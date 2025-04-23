import psycopg2
import os 
import google.generativeai as genai
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from firebase_init import db


# connect to postgreSQL(del)
def get_conn():
  load_dotenv(dotenv_path='.env')
  conn = psycopg2.connect(
      dbname = os.getenv("dbname"),
      user = os.getenv("user"),
      password = os.getenv("password"),
      host = os.getenv("host"),
      port = os.getenv("port")
  )
  print("connect to PostgreSQL successfully")

  return conn


# get resume data for static resume website(del)
def get_resume_data_for_static(cursor, table, col, resume_data):
    for i in range(len(col)):
        database = table[i]
        column = col[i]
        query = f"SELECT {', '.join(column)} FROM {database}"
        if i == 2: # skill
            query = """
                SELECT category, STRING_AGG(tools, '、') AS tool_list
                FROM skill
                GROUP BY category;
            """           
        cursor.execute(query)
        data = cursor.fetchall()
        #resume_data.append({database: [dict(zip(column, row)) for row in data]})
        resume_data[database] = [dict(zip(column, row)) for row in data]
    print(resume_data)

    return resume_data


# connect to firestore and get resume data
# https://blog.csdn.net/weixin_44346972/article/details/106747178
def get_firestore_data(resume_data):
    docs = db.collection("resume").stream()
    for doc in docs:
        resume_data.update(doc.to_dict())
    #print(resume_data)
    
    return resume_data
        

# according to system 2, get resume data for chating(del)
def get_resume_data_for_dynamic(cursor, main_response, exp_response):
    if int(main_response) != 9:
        query = "SELECT description FROM main_class WHERE class_id = " + main_response + ";"
    elif int(main_response) == 9:
        query = "SELECT description FROM exp_class WHERE class_id = " + exp_response + ";" 
    print(query)
    cursor.execute(query)
    data = cursor.fetchall() # 再看看有沒有要整理格式

    return data


# get data from firebase
def get_ref(table):
    doc_ref = db.collection("resume").document(table)
    doc = doc_ref.get()
    if doc.exists:
        class_list = ''
        doc_dict = doc.to_dict()
        for d in doc_dict[table]:
            class_id = d['class_id']
            classifier = d['classifier']
            string = str(class_id)+' '+classifier+'\n'
            class_list += string
        return doc_dict, class_list
    else:
        print("No such document!")
        return None


'''
doc_dict, class_list = get_ref('main_class')
print(class_list)

doc_dict, class_list = get_ref('exp_class')
print(class_list)

doc_dict, class_list = get_ref('else_class')
print(class_list)
'''

# insert chat history into firebase(del)
def insert_chat_his(user_id, records):
    doc_ref = db.collection("resume").document("chat_history")
    update_data = {
        f"{user_id}": firestore.ArrayUnion(records)
    }
    doc_ref.set(update_data, merge=True)
    print("Chat history inserted into Firebase!")

# insert data into firebase
def insert_data_to_firebase(doc, user_id, data):
    doc_ref = db.collection("resume").document(doc)
    update_data = {
        f"{user_id}": firestore.ArrayUnion(data)
    }
    doc_ref.set(update_data, merge=True)
    print(f"{doc} inserted into Firebase!")
# insert_data_to_firebase("chat_history", user_id, records)
# insert_data_to_firebase("feedback", user_id, feedback)

