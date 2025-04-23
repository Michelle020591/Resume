import psycopg2
from flask import Flask, render_template, session, request, jsonify, send_file
import os 
import re
from google import genai
from google.genai import types
from dotenv import load_dotenv
import database
import service
import arch.config as config


app = Flask(__name__)


resume_data = {} 
chat_history = []

@app.route("/")
def resume():
    # connect to postgreSQL
    #conn = database.get_conn()
    #cursor = conn.cursor()

    # target table, column
    #table = config.table
    #col = config.col

    # get resume data for website
    #static_resume_data = database.get_resume_data_for_static(cursor, table, col, resume_data)
    
    # close postgreSQL
    #ursor.close()
    #conn.close()

    static_resume_data = database.get_firestore_data(resume_data)

    return render_template("index.html", data=static_resume_data)


@app.route("/chat", methods=["post"])
def chat():
    # connect to postgreSQL
    #conn = database.get_conn()
    #cursor = conn.cursor()

    # access to Gemini
    #genai.configure(api_key=service.get_gemini_key())
    #model_1 = genai.GenerativeModel("gemini-2.0-flash")
    #model_2 = genai.GenerativeModel("gemini-1.5-flash")

    # get user question/id
    user_id = request.get_json().get('user_id')
    user_input = request.get_json().get('message')

    # detect incorrect spelling
    spell_response, incorrect_spelling = service.incorrect_spelling(user_input)

    # get reference: 1. relative chat history; 2. database resume data
    # filter = service.filter_relative_chat_history(model, user_input)
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
    # response = service.generate_response(model_1, user_input, filter, dynamic_resume_data)

    # record chat history
    records = service.record_chat_history(chat_history, user_input, ques_response, spell_response, main_id, exp_id, else_id)
    database.insert_data_to_firebase("chat_history", user_id, records)
    #database.insert_chat_his(user_id, records)

    # close postgreSQL
    #cursor.close()
    #conn.close()

    if incorrect_spelling:
        return jsonify({
            "spell_response": spell_response,
            "ques_response": ques_response
        })
    else:
        return jsonify({
            "ques_response": ques_response
        })
    

# 
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

"""
        rating = user_feedback.get("rating")
        attract = user_feedback.get("attract")
        suggestion = user_feedback.get("suggestion")
        company = user_feedback.get("company")
        identity = user_feedback.get("identity")
        email = user_feedback.get("email")
        print([user_id, rating, attract, suggestion, company, identity, email])




@app.route("/feedback_data", methods=["POST"])
def feedback_data():
    user_input = request.get_json()
    print(user_input)
    rating = user_input.get('rating')
    attract = user_input.get('attract')
    suggestion = user_input.get('suggestion')

    print(rating)
    print(attract)
    print(suggestion)

    # 處理資料...
    return jsonify({"status": "success", "message": "資料接收成功"})

"""





if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)