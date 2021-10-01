from flask import Flask, render_template
import mysql.connector      #   import du client mysql
import json

#   connection au serveur mysql
db = mysql.connector.connect(
  host="localhost",
  port=3307,
  user="root",
  password="root",
  database="webapp"
)

app = Flask(__name__)

@app.route("/")
def home():
    return "ok"

@app.route("/student")
def student():
    cursor = db.cursor()
    cursor.execute("select * from student")
    students = cursor.fetchall()    #   convertir les resultats sql en structure du langage python
    #print(students)
    #return json.dumps(students)    #   envoie des données au format JSON
    return render_template("student.html", students=students)

@app.route("/student/<id>")
def studentDetail(id):
    cursor = db.cursor()
    sql = "select firstname, note from student where id = %s"
    params = (id, )
    cursor.execute(sql, params)
    studentFirstname, studentNote = cursor.fetchall()[0]
    #print(studentInfo)
    return studentFirstname + " a obtenu la note de : " + str(studentNote) +"/20"

@app.route("/meanStudentsList")
def meanStudents():
    cursor = db.cursor()
    cursor.execute("select firstname, lastname from student where note >= 10")
    studentsList = cursor.fetchall()
    return render_template("meanStudents.html", students=studentsList)

#   démarrage du serveur
app.run(host="0.0.0.0", port=8080)
