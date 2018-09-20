from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hey man"

@app.route("/first")
def func2():
    return "hey dude"

@app.route("/second")
def func3():
    return "hey guy"


if __name__ == "__main__":
    app.debug = True
    app.run()

