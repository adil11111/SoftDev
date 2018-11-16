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
    url = urllib.request.urlopen("https://dog.ceo/api/breeds/image/random")
    info = json.loads(url.read())
    #print (info)


    url = urllib.request.urlopen("http://xkcd.com/231/info.0.json")
    info1 = json.loads(url.read())
    #print (info1)

    url = urllib.request.urlopen("https://catfact.ninja/fact")
    info2 = json.loads(url.read())
    print (info2)


    return render_template("index.html",dog=info['message'],xkcd = info1['img'],cat=info2['fact'])

if __name__ == "__main__":
    app.debug = True
    app.run()
