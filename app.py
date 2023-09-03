
from flask import Flask,render_template,request,redirect,url_for,session,jsonify,Response
from flask import Flask,render_template, request
from flask_mysqldb import MySQL
import json
import datetime
import os
import time
import datetime
import winsound

app = Flask(__name__)
 

 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'enaissance' 
mysql = MySQL(app)




@app.route("/login",methods=["GET"])
def login():
    name=request.args.get('name')
    password=request.args.get('password')
    return render_template("index1.html",name=name,password=password)

@app.route("/login_ver",methods=["POST","GET"])
def login_ver():
    if request.method == "POST":
        donnees=request.form
        name=request.form.get("name")
        password=request.form.get("password")
        
       
        return redirect(url_for("index"))    
    else:
        return redirect(url_for("login"))

@app.route("/")
def index():
    
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM declaration''')
    rv = cur.fetchall()
    compteur=0
    while compteur < len(rv):
        print(rv[compteur])
        compteur=compteur+1
        
    return render_template("index.html",liste_declaration=rv)


@app.route("/register")
def register():
    return render_template("sign-up.html")



@app.route("/register_ver", methods=["POST"])
def register_ver():
    if request.method == "POST":
        email=request.form.get("email")
        name=request.form.get("name")
        password=request.form.get("password")
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO administrateur VALUES(" ",%s,%s,%s)''',(email,name,password))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('login',name=name,password=password))
    else:
        return redirect(url_for('register'))

@app.route("/schedule_exam")
def schedule_exam():
    exam_liste=['1','2','3']
    return render_template("schedule-exam.html",exam_list=exam_liste)

@app.route("/naissance")
def naissance():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM declaration''')
    rv = cur.fetchall()
    compteur=0
    while compteur < len(rv):
        print(rv[compteur])
        compteur=compteur+1
    return render_template("naissance.html",liste_declaration=rv)

@app.route("/launch_exam_2camera")
def launch_exam_2camera():
    return render_template("launch-exam-2camera.html")

@app.route("/live_exam_gate")
def live_exam_gate():
    return render_template("live-exam-gate.html")

@app.route("/live_exam_gate_face")
def live_exam_gate_face():
    image_folder = 'static'  # Nom du dossier contenant les images
    image_list = os.listdir(image_folder)
    return render_template("live-exam-gate-face.html",image_list=image_list[4:])

@app.route("/view_report")
def view_report():
    return render_template("view-report.html")

@app.route("/live_video")
def live_video():
    return render_template("live-video.html")


@app.route("/students_management")
def students_management():
    return render_template("student-management.html")

@app.route("/create_student")
def students():
    return render_template("create-student.html")

@app.route("/students_reg",methods=["POST"])
def students_reg():
        return redirect(url_for('students_management'))
 
@app.route("/classroom_level")
def classroom_level():
    return render_template("classroom_level.html")

@app.route("/subscription")
def subscription():
    return render_template("subscription.html")

@app.route("/create_exam")
def create_exam():
    return render_template("create-exam.html")

@app.route("/create_exam_reg",methods=["POST"])
def create_exam_reg():
    if request.method == "POST":
        exam_code=request.form.get("exam_code")
        subject=request.form.get("subject")
        classroom_name=request.form.get("classroom_name")
        exam_date=request.form.get("exam_date")
        date=exam_date.split('-')
        start_time=request.form.get("start_time")
        time=start_time.split(':')
        class_name=request.form.get("class_name")
        duration=request.form.get("duration")
        assignee=request.form.get("assignee")
        status="To be done"
        report="../reports/"
        print('start time {} exam date {} duration {}  '.format(start_time,exam_date,duration))
       
        return redirect(url_for('schedule_exam'))
   

@app.route("/live_exam")
def live_exam():
    return render_template("live-exam.html")

@app.route("/live_exam_surveillance")
def live_exam_surveillance():
    
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/live_video_class")
def live_video_class():
    return render_template("live-video-class.html")

@app.route("/live_video_class2")
def live_video_class2():
    return render_template("live-video-class2.html")



if __name__=="__main__":
    app.run(debug=True)
    
    
