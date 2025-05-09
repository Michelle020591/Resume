import os 
import re
from google import genai
from google.genai import types
from dotenv import load_dotenv
from datetime import datetime


# Gemini login
def get_gemini_key():
    api_key = os.environ.get("gemini_key")
    #load_dotenv(dotenv_path='.env')
    #api_key = os.getenv("gemini_key")
    print("Got Gemini Key!")
    return api_key


# generate response
def gen_response(prompt, model = "gemini-2.0-flash", temperature = 0):
    client = genai.Client(api_key=get_gemini_key())
    response = client.models.generate_content(
        model = model, 
        contents = prompt,
        config = types.GenerateContentConfig(
            temperature = temperature,
            system_instruction = [
            types.Part.from_text(text="""你是宣葇的AI小助手，用輕鬆但帶有專業的語氣回答使用者的問題，不用說哈囉或強調你是宣葇AI小助手"""),
        ])
    )
    return response.text


# system 1: detect incorrect spelling
def incorrect_spelling(user_input):
    incorrect_spelling = False
    prompt = f"""
        請檢查這段文字：「{user_input}」是否有錯字
        若有錯字，例如，輸入：請字我介紹
        請回答：是「自」我介紹 ^_^b
        只需要將錯字刪除後，以「」標記正確的字取代並加上 ^_^b
        若沒有錯字，請回答：完全正確
        """
    model = "gemini-1.5-flash"
    response = gen_response(prompt, model)
    match = re.search(r"(正確|完全正確|拼音正確)", response)
    if not(match):
        incorrect_spelling = True
    print(response)

    return response, incorrect_spelling


# system 2: classify question number
def classify_question(user_input, classifier, exp_classifier, else_classifier):
    prompt = f"""
        請判斷問題：「{user_input}」
        屬於{classifier}中哪種分類編號（單選）
        請以分類編號(阿拉伯數字）回答
        """
    #若為複選，請將數字以/分隔。

    main_response = gen_response(prompt)
    print("main_class:"+main_response)

    exp_response = None
    else_response = None
    if int(main_response) == 9: #經驗

        prompt = f"""
            請判斷問題：「{user_input}」
            屬於{exp_classifier}中哪種分類編號（單選）
            請以分類編號(阿拉伯數字）回答
        """
        exp_response = gen_response(prompt)
        print("exp_class:"+exp_response)

    if int(main_response) == 0: #其他
        prompt = f"""
            請判斷問題：「{user_input}」
            屬於{else_classifier}中哪種分類編號（單選）
            請以分類編號(阿拉伯數字）回答
        """
        else_response = gen_response(prompt)
        print("else_class:"+else_response)

    return main_response, exp_response, else_response


# system 3: generate answer
def generate_response(user_input, resume_data, main_response): 
    if int(main_response) == 10 or int(main_response) == 0: #情境或其他
        prompt = f"""
            問題：{user_input}\n{resume_data}
            """
        response = gen_response(prompt, temperature=0.15)

    else:
        prompt = f"""
            只能根據以下履歷資料：{resume_data}\n
            回答問題：{user_input}
            如果問題的主詞是「你」或是沒有提及主詞，預設在問宣葇
            回答方式：幫宣葇回答問題，100字為限
            若要列點，請用米字號將標題標記出來，例如：**標題**
            """
        response = gen_response(prompt)
    
    print(prompt)
    print(response)

    return response


# record chat history
def record_chat_history(chat_history, user_input, main_response, word_response, main_id, exp_id, else_id):
    his_dict = {
        "user": str(user_input),
        "class_id": f"{main_id}/{exp_id}/{else_id}",
        "assistant": f"main: {main_response} word: {word_response}",
        "time": datetime.now().isoformat()
    }
    print(his_dict)
    chat_history.append(his_dict)
    print("Append into chat history successfully!")

    return chat_history

# record feedback 
def record_feedback(fb_dict):
    fb_lst = []
    fb_lst.append(fb_dict)

    return fb_lst
