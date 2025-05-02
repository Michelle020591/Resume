from flask import Flask, render_template, request, jsonify
import os 
import re
from google import genai
from google.genai import types
from dotenv import load_dotenv
import database
import service


app = Flask(__name__)



resume_data = {} 
chat_history = []

@app.route("/")
def resume():
    static_resume_data = database.get_firestore_data(resume_data)

    return render_template("index.html", data=static_resume_data)



@app.route("/chat", methods=["post"])
def chat():
    # get user question/id
    user_id = request.get_json().get('user_id')
    user_input = request.get_json().get('message')

    # detect incorrect spelling
    spell_response, incorrect_spelling = service.incorrect_spelling(user_input)

    # get reference: database resume data
    main_ref, main_class_lst = database.get_ref('main_class')
    exp_ref, exp_class_lst = database.get_ref('exp_class')
    else_ref, else_class_lst = database.get_ref('else_class')

    main_id, exp_id, else_id = service.classify_question(user_input, main_class_lst, exp_class_lst, else_class_lst)
    if int(main_id) == 0:
        ref = else_ref['else_class'][int(else_id)-1]['description']
    elif int(main_id) == 9:
        ref = exp_ref['exp_class'][int(exp_id)-1]['description']
    else:
        ref = main_ref['main_class'][int(main_id)-1]['description']
    print(ref)

    # generate response
    ques_response = service.generate_response(user_input, ref, main_id)
    print(type(ques_response))
    if (int(main_id) == 0 and else_id != None and int(else_id) == 1) or (int(main_id) == 17):
        ques_response += '''<button class="feedback-btn" onclick="jumpToFeedback()">填寫回饋表單</button>'''
        print(ques_response)

    # record chat history
    records = service.record_chat_history(chat_history, user_input, ques_response, spell_response, main_id, exp_id, else_id)
    database.insert_data_to_firebase("chat_history", user_id, records)

    if incorrect_spelling:
        return jsonify({
            "spell_response": spell_response,
            "ques_response": ques_response
        })
    else:
        return jsonify({
            "ques_response": ques_response
        })



@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "GET":
        return render_template('feedback.html')
    
    elif request.method == "POST":
        user_feedback = request.get_json()
        print(user_feedback)
        user_id = user_feedback.get("user_id")
        del user_feedback["user_id"]
        feedback = service.record_feedback(user_feedback)
        database.insert_data_to_firebase("feedback", user_id, feedback)
      
        return jsonify({"status": "success", "message": "資料接收成功"})



if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)