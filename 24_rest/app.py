#Adil Gondal
#SoftDev1 pd07
#K24- A RESTful Journey Skyward
#2018-11-13

from flask import Flask, render_template
import urllib.request
import json
app = Flask(__name__)

@app.route("/")
def root():
    url = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=NNKOjkoul8n1CH18TWA9gwngW1s1SmjESPjNoUFo")
    info = json.loads(url.read())
    print (info)
    return render_template("index.html",pic=info['url'],explanation = info['explanation'])

if __name__ == "__main__":
    app.debug = True
    app.run()

