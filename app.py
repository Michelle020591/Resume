import psycopg2
from flask import Flask, render_template
import requests
import jsonify
import openai

app = Flask(__name__)

# connect to postgreSQL
def get_conn():
  conn = psycopg2.connect(
      dbname = "postgres",
      user = "jack",
      password = "12345678",
      host = "localhost"
  )
  print("connect to PostgreSQL successfully")

  return conn


# get resume data
resume_data = {} #resume_data = []
def get_info(cursor, db, col, resume_data):
    for i in range(len(col)):
        database = db[i]
        column = col[i]
        query = f"SELECT {', '.join(column)} FROM {database}"
        if i == 2: # skill
            query = """
                SELECT category, STRING_AGG(tools, ', ') AS tool_list
                FROM skill
                GROUP BY category;
            """           
        cursor.execute(query)
        data = cursor.fetchall()
        #resume_data.append({database: [dict(zip(column, row)) for row in data]})
        resume_data[database] = [dict(zip(column, row)) for row in data]
    print(resume_data)

    return resume_data


# connect to postgreSQL and get resume data
def wrap():
   global resume_data
   conn = get_conn()
   cursor = conn.cursor()
   resume_data = get_info(cursor, db, col, resume_data)
   cursor.close()
   conn.close()

   return resume_data


# OpenAI login
# https://realnewbie.com/basic-concent/how-to-obtain-openai-api-key-step-by-step-guide/
# openai.api_key = "sk-xxxxxxxxxx"



## main function starts here ##

db = [
    "user_info",
    "education",
    "skill",
    "language",
    "advantage",
    "experience",
    "work_skill",
    "project"
]

col = [
    ["ch_name", "en_name", "email", "phone", "github", "address"],
    ["start_date", "end_date", "school", "class"],
    ["category", "tools"],
    ["category", "test"],
    ["advantage", "description"],
    ["company", "role", "start_date", "end_date", "description"],
    ["work_id", "category", "description"],
    ["title", "skill", "description"]
]


@app.route("/")
def resume():
    resume_data = wrap()
    return render_template("index.html", data=resume_data)


@app.route('/assistant')
def assistant():
    return render_template('assistant.html')


"""
records = {}

@app.route("/chat", methods=["post"])
def chat(records):
    resume_data = wrap()
    # get user question
    user_question = requests.json.get("input")
    prompt = f"根據以下履歷資料：{resume_data}\n\n回答問題：{user_question}"
    print(prompt)

    # short-term memory
    if "chat_history" not in records:
        records["chat_history"] = [{"role": "system", "content": "你是一個專業的履歷Chatbot，可以根據履歷資料回答使用者問題"}]

    records["chat_history"].append({"role": "user", "content": prompt})
"""
"""
  # send question to OpenAI
  response = openai.ChatCompletion.create(
      model = "gpt-3.5-turbo",
      messages = records["chat_history"]
  )

  print(response) # 資料型態未知！！！

  #
  records["chat_history"].append({"role": "assistant", "content": response})

  return jsonify({"response": response})"
"""


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)






