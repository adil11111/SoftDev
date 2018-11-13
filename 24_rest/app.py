from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def root():
    u = urllib.urlopen("https://api.nasa.gov/planetary/apod?api_key=NNKOjkoul8n1CH18TWA9gwngW1s1SmjESPjNoUFo")
    return render_template("index.html",pic = data['url'])


if __name__ == "__main__":
    app.debug = True
    app.run()

