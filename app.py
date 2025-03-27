from flask import Flask, render_template
from google.cloud.sql.connector import Connector

app = Flask(__name__)

# connect to cloud sql
connection_name = "clean-pilot-454602-v1:asia-east1:resume-db"
driver = "pg8000"
db_user = "postgres"
db_pass = "10350036"
db_name = "resume_db"

def getconn():
    connector = Connector()
    conn= connector.connect(
        connection_name,
        driver,
        user = db_user,
        password = db_pass,
        db = db_name,
    )
    print("connect to cloud SQL successfully")

    return conn


# data columns, database needed 
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


# get resume information
data_list = {} #data_list = []
def get_info(cursor, db, col, data_list):
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
        #data_list.append({database: [dict(zip(column, row)) for row in data]})
        data_list[database] = [dict(zip(column, row)) for row in data]

    return data_list


@app.route("/")
def resume():
    conn = getconn()
    cursor = conn.cursor()
    data = get_info(cursor, db, col, data_list)
    print(data)
    cursor.close()
    conn.close()
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)


"""
render_template('index.html', data=rows)
def getconn():
    conn= connector.connect(
        connection_name,
        driver,
        db_user,
        db_pass,
        db_name
    )
    return conn
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+pg8000://"
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {"creator":getconn}
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

@app.route("/test_db")
def test_db():
    
    cursor.execute("SELECT 'Database Connected!'")
    result = cursor.fetchone()
    cursor.close()
    return result[0]

"""
