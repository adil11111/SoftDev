from flask import Flask, render_template , request
app = Flask(__name__)


@app.route("/")
def func():
    print(app)
    return render_template("form.html")
@app.route("/auth",methods = ["GET","POST"])
def authenticate():
    print(app)
    print(request)
    print(request.args)
    #print(request.args['username'])
    #print(request.method)
    result = request.args['username']
    method=request.method
    return render_template("form2.html",name=result,methodUsed=method)


if __name__ == "__main__":
    app.debug = True
    app.run()

