#A Dill Pickle -- Adil Gondal and Jason Lin
#SoftDev1 pd07
#K15 -- Oh yes, perhaps I do...
#2018-10-02

from flask import Flask, render_template, request
from flask import session, url_for, redirect, flash
import os
app = Flask(__name__) # instantiates an instance of Flask

app.secret_key = os.urandom(32) #generates a secret key

@app.route("/")
def login():
    # Checks if there was a previous session and redirect or render accordingly
    if "username" in session:
        return redirect(url_for("welcome"))
    else:
        return render_template("login.html")

@app.route("/auth", methods=["POST"])
def auth():
    # Gets the username and password from form
    username=request.form["username"]
    password= request.form["password"]

    # Checks if username and password is correct
    # If not, then redirect back to login page with flash message
    # If correct, creates a session and goes to welcome page
    if username == "Adil":
            if password=="Jason":
                session["username"] = username
                return redirect(url_for("welcome"))
            else:
                flash("Wrong Password!")
                return redirect(url_for("login"))
    else:
        flash("Wrong Username!")
        return redirect(url_for("login"))

@app.route("/welcome")
def welcome():
    # Checks if a session exists and renders or redirects accordingly
    if "username" in session:
        return render_template("welcome.html",user=session["username"])
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    # Removes session when user logs out and redirects back to login page
    session.pop("username")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.debug = True
    app.run()
