from flask import Flask
from flask import redirect, render_template, request, session
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    
    sql = "SELECT password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()   
    #check if user is in database 
    if user == None:
        return redirect("/login")
    else:
        hash_value = user[0]
        if check_password_hash(hash_value,password):
            #login successful

            session["username"] = username
            return redirect("/forum")
        else:
            #wrong password
            return "<p>väärin</p>"

    session["username"] = username
    return redirect("/forum")

# Broken method for creating new users

# @app.route("/signup",methods=["POST"])

# def signup():
#     username = request.form["username"]
#     password = request.form["password"]

#     hash_value = generate_password_hash(password)
#     sql = "INSERT INTO users (username,password) VALUES (:username,:password)"
#     db.session.execute(sql, {"username":username,"password":hash_value})
#     db.session.commit()


@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")




#Main page for accessing discussion zones 
@app.route("/forum")
def forum():
    result = db.session.execute("SELECT * FROM zones ORDER BY name")
    zones = result.fetchall()
    return render_template("forum.html", zones = zones)

#Page for discussion zone
@app.route("/forum/<int:zone_id>")
def zone(zone_id):
    sql = "SELECT * FROM threads WHERE zone_id =" + str(zone_id) 
    result = db.session.execute(sql)
    threads = result.fetchall()
    sql = "SELECT name,description,id FROM zones WHERE id ="+ str(zone_id)
    result = db.session.execute(sql)
    zone_info = result.fetchall()
    return render_template("zone.html", threads = threads, zone = zone_info)

#Page for single thread
@app.route("/forum/<int:zone_id>/<int:thread_id>")
def thread(zone_id,thread_id):
    sql = "SELECT M.msg,U.username,M.posted_at FROM messages M, users U WHERE M.thread_id \
        =" + str(thread_id) + " AND M.poster_id = U.id ORDER BY M.posted_at"
    result = db.session.execute(sql)
    messages = result.fetchall()
    sql = "SELECT T.subject, T.created_at, U.username, T.id,T.zone_id\
        FROM threads T, users U WHERE T.id ="+ str(thread_id) +"\
         AND U.id = T.started_by"
    result = db.session.execute(sql)
    thread_info = result.fetchall()

    return render_template("thread.html", messages = messages, thread = thread_info)

@app.route("/postmsg", methods=["POST"])
def postmsg():
    sql = "SELECT id FROM users WHERE username = '"+ session["username"] + "'"
    result = db.session.execute(sql)
    user_id = result.fetchone()[0]
    thread_id = request.form["thread_id"]
    zone_id = request.form["zone_id"]
    message = request.form["message"]
    
    sql = "INSERT INTO messages (poster_id,msg,thread_id,posted_at)\
        VALUES ("+ str(user_id) + ", '" + message + "', "+ str(thread_id) + ", NOW())"

    db.session.execute(sql)
    db.session.commit()
    return redirect("/forum/"+ str(zone_id) +"/"+ str(thread_id))
    


