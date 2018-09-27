from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hsdsado queso!"

app.debug = True
app.run()


app.debug = True
app.run()
