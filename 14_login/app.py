#Adil Gondal
#SoftDev1 pd07
#K14 -- Do I Know You?
#2018-10-02

from flask import Flask, render_template, request ,session,url_for,redirect
import os
app = Flask(__name__) # instantiates an instance of Flask

@app.route("/") #Linking a function to a route
def home():
    print(url_for('home'))
    return redirect(url_for("login"))#render_template("template.html")

@app.route("/auth", methods=["POST"]) 
def auth():
    username=request.form["username"]
    password= request.form["password"]
    if username == "Bob":
            if password=="pizza":
                return render_template("login.html",user=username)
            else:
                return render_template("error.html",error_message="Wrong password")
    else:
        return render_template("error.html",error_message="Wrong Username")

@app.route("/login")
def login():
    return render_template("template.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
