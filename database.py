from dotenv import load_dotenv
from firebase_admin import firestore
from firebase_init import db

# connect to firestore and get resume data
# https://blog.csdn.net/weixin_44346972/article/details/106747178
def get_firestore_data(resume_data):
    docs = db.collection("resume").stream()
    for doc in docs:
        resume_data.update(doc.to_dict())
    #print(resume_data)
    
    return resume_data


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

