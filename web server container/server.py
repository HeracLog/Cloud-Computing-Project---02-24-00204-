from flask import Flask, request, jsonify, abort
import random
import psycopg2
from flask_cors import CORS, cross_origin
import time

app = Flask(__name__,static_url_path='/static')
CORS(app, support_credentials=True)
app.config['CORS_HEADERS'] = 'application/json'

tries = 0
max_tires = 5

while tries < max_tires :
    try:
        conn = psycopg2.connect(database = "Students", 
                                user = "postgres", 
                                host= 'database',
                                password = "admin",
                                port = 5432)
        break   
    except:
        tries+=1
        time.sleep(10)

    

def parseAdminHomepage():
    with open('./templates/home.html','r') as f:
        pageData = f.read()
    cur = conn.cursor()
    cur.execute('SELECT * FROM STUDENTS;')
    studentData= cur.fetchall()
    conn.commit()
    cur.close()
    entries = []
    for student in studentData:
        entries.append(
            f"""
            <tr>
                <td><a href="/student/{student[0]}">{student[1]}</a></td>
                <td>{student[0]}</td>
                <td>{student[-1]}</td>
            </tr>
            """
        )
    return pageData.replace(
        'STUDENTDATAGOESHERE','\n'.join(entries)
    )

def parseStudentHomepage(id):
    with open('./templates/stud_prof.html','r') as f:
        pageData = f.read()
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM STUDENTS WHERE studentID = {id};')
    studentData= cur.fetchall()
    conn.commit()
    cur.close()
    entries = []
    for student in studentData:
        entries.append(
            f"""
            <h2>Name: {student[1]}</h2>
            <p>ID: {student[0]}</p>
            <p>Age: {student[2]}</p>
            <p>Department: {student[-1]}</p>
            <p>Level: {student[-3]}</p>
            <p>CGPA: {student[-2]}</p>
            """
        )
    return pageData.replace(
        'STUDENTDATAGOESHERE','\n'.join(entries)
    )


def generateToken():
    parseAdminHomepage()
    return ''.join(random.choices(
        population='abcdefghijklmnopqrstuvwxwz1234567890!@#$%^&*()', k=128))

# Key is token, value is access type
access_tokens = {}
@app.after_request
def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true,X-Requested-With')
        response.headers.add('Access-Control-Allow-Credentials',True)
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        response.headers.add('Access-Control-Allow-Origin', '*')

        return response

@app.route('/login/<username>/<password>')
def login(username, password):
    cur = conn.cursor()
    cur.execute('SELECT * FROM USERS;')
    rows = cur.fetchall()
    conn.commit()
    cur.close()
    for row in rows:
        if row[1] == username and row[2] == password:
            token = generateToken()
            if row[3]:
                access_tokens.update({token:"admin"})
                return parseAdminHomepage()
            else:
                access_tokens.update({token:"user"})
                return parseStudentHomepage(row[1])
    abort(403)

@app.route('/')
def loginPage():
    with open('./templates/index.html','r') as f:
        return f.read()
@app.route('/student/<id>')
def accessStudentData(id):
   return parseStudentHomepage(id)

app.run(host='0.0.0.0',port=7000,debug=True)
