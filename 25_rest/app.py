#Adil Gondal
#SoftDev1 pd07
#K25- A RESTful Journey Skyward
#2018-11-13

from flask import Flask, render_template
import urllib.request
import json
app = Flask(__name__)

@app.route("/")
def root():
    url = urllib.request.urlopen("http://api.icndb.com/jokes/random?limitTo=[nerdy]")
    info = json.loads(url.read())
    #print (info)
    #print(info['value']['joke'])
    return render_template("index.html",joke = info['value']['joke'])

if __name__ == "__main__":
    app.debug = True
    app.run()

