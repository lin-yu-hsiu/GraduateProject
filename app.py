from flask import Flask, redirect,render_template, url_for,request,jsonify
import DB,json

app = Flask(__name__)

@app.route("/")             #切換 URL
def hello():
    content = DB.show_data('User')
    print(json.dumps(content))
    return jsonify(content)
@app.route("/login",methods = ['POST','GET'])
def login():
    return render_template("login.html")
@app.route("/index",methods = ['POST','GET'])
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()