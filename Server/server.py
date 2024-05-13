from flask import Flask, abort, send_from_directory
import psycopg2
from flask_cors import CORS 
import time

# Startng flask app with the file name and defining the static file path
app = Flask(__name__,static_url_path='/static')
# Adding CORS to the server
CORS(app, support_credentials=True)

# Defining number of tries of connecting to the database
tries = 0
max_tires = 5

# Trying to connect
while tries < max_tires :
    try:
        # Creates database connection
        conn = psycopg2.connect(database = "Students", # Database name 
                                user = "postgres", # Database user
                                host= 'database', # Service name in docker-compose
                                password = "admin", # Database password
                                port = 5432) # Database port
        break   
    except:
        # If connection isn't succesful we try again after 10 seconds
        tries+=1
        time.sleep(10)

    
# Function for parsing admin homepage
def parseAdminHomepage():
    # Opens the admin file and reads the data 
    with open('./templates/home.html','r') as f:
        pageData = f.read()
    # Creates a cursor to the database
    cur = conn.cursor()
    # Selects all students
    cur.execute('SELECT * FROM STUDENTS;')
    # Stores the fetched data
    studentData= cur.fetchall()
    # Commits changes
    conn.commit()
    # Closes the cursor
    cur.close()
    # Empty entries list
    entries = []
    # Loops through all students
    for student in studentData:
        # Appends the html data for the student
        entries.append(
            f"""
            <tr>
                <td><a href="/student/{student[0]}">{student[1]}</a></td>
                <td>{student[0]}</td>
                <td>{student[2]}</td>
                <td>{student[-2]}</td>
                <td>{student[-3]}</td>
                <td>{student[-1]}</td>
            </tr>
            """
        )
    # Returns the data after joining the entries and replacing the placeholder
    return pageData.replace(
        'STUDENTDATAGOESHERE','\n'.join(entries)
    )

# Parsing Student Homepage 
def parseStudentHomepage(id):
    # Opens student homepage and reads the data
    with open('./templates/stud_prof.html','r') as f:
        pageData = f.read()
    # Creates a cursor to the database
    cur = conn.cursor()
    # Selects student with given id
    cur.execute(f'SELECT * FROM STUDENTS WHERE studentID = \'{id}\';')
    # Stores the fetched data
    studentData= cur.fetchall()
    # Commits changes
    conn.commit()
    # Closes the cursor
    cur.close()
    # Creates empty string for student entry
    entry = ''
    for student in studentData:
        # Formats student data
        entry = f"""\n
            <h2>Name: {student[1]}</h2>
            <p>ID: {student[0]}</p>
            <p>Age: {student[2]}</p>
            <p>Department: {student[-1]}</p>
            <p>Level: {student[-3]}</p>
            <p>CGPA: {student[-2]}</p>
            """
    # Returns the page after replacing the placeholder
    return pageData.replace(
        'STUDENTDATAGOESHERE',entry)

# CORS headers
@app.after_request
def after_request(response):
    # Adds the response headers for the request
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true,X-Requested-With')
    response.headers.add('Access-Control-Allow-Credentials',True)
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Origin', '*')
    # Returns the request
    return response

# Main route
@app.route('/')
def loginPage():
    # Reads and returns the login page
    with open('./templates/index.html','r') as f:
        return f.read()

# Login route
@app.route('/login/<username>/<password>')
def login(username, password):
    # Creates a cursor to the database
    cur = conn.cursor()
    # Selects all users
    cur.execute('SELECT * FROM USERS;')
    # Stores the fetched data
    rows = cur.fetchall()
    # Commits the changes
    conn.commit()
    # Closes the cursor
    cur.close()
    # Loops though all entries
    for row in rows:
        # If the username and password match up
        if row[1] == username and row[2] == password:
            # If the user is an admin user, we send the admin homepage
            if row[3]:
                return parseAdminHomepage()
            # Otherwise we send the user homepage
            else:
                return parseStudentHomepage(row[1])
    # If the credentials are wrong, we reply with a 'forbidden' response
    abort(403)

# Student data route
@app.route('/student/<id>')
def accessStudentData(id):
   # Returns the student page    
   return parseStudentHomepage(id)
    

# Adding a student route
@app.route('/add/<name>/<id>/<age>/<level>/<dep>/<cgpa>')
def addStudent(name,id,age,level,dep,cgpa):
    # Tries to add the student
    try:
        # Creates a cursoe to the database
        cur = conn.cursor()
        # Fetches entries with the given id to check if user exists
        cur.execute(f'SELECT * FROM STUDENTS WHERE studentID = \'{id}\';')
        # Stores the fetched data
        data = cur.fetchall()
        # If the entry already exists
        if data:
            # Raise an exception
            raise Exception("Student Already exists")
        # Executes the insert operation
        cur.execute(f"""INSERT INTO STUDENTS VALUES 
    ('{id}', '{name}', {age},{level},{cgpa},'{dep}' );""")
        # Commits the changes
        conn.commit()
        # Closes the cursor
        cur.close()
        # Returns OK
        return ""
    # If an exception does occur
    except Exception as e:
        print(e)
        # Return the error page
        abort(400)

# Adding page route
@app.route('/add-std')
def add():
    # Reads and returns the add student page
    with open('./templates/add_stud.html','r') as f:
        return f.read() 

# Favicon route
@app.route('/favicon.ico')
def favicon():
    # Reads the icon from the directory, add the mimetype and returns the file
    return send_from_directory(app.root_path, 'favicon.ico', mimetype='image/vnd.microsoft.icon')


# Runs the app on host '0.0.0.0' and port 7000, with debugging on
app.run(host='0.0.0.0',port=7000,debug=True)
