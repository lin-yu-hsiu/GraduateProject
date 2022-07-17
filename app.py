from unittest import result
from flask import Flask, redirect,render_template, url_for,request,jsonify
from jinja2 import Undefined
from flask_cors import CORS
import DB,json

app = Flask(__name__)
CORS(app)
@app.route("/")             #切換 URL
def Home():
    return "Home Page"

@app.route("/table/<name>")
def table(name):
    content = DB.show_data(name)
    try:
        return jsonify(content)
    except TypeError as e:
        return str(content)

@app.route("/create/<name>")
def insert(name):
    data = {
        "UUID": "testUUID2",
        "MessageNum": 17,
        "MapNum":1,
        "Xaxis":100,
        "Yaxis":100,
        "Battery":'0%',
        "Status": 0,
        "Place": "服務台"
    }
    result = DB.insert_data(name,data)
    if(result['success']):
        return jsonify(result)
    else:
        return jsonify(result)

@app.route("/delete/<name>")
def delete(name):
    pk = 3
    result = DB.delete_data(name,pk)
    if(result['success']):
        return jsonify(result)
    else:
        return jsonify(result)

@app.route("/deleteAll/<name>")
def deleteAll(name):
    result = DB.delete_all(name)
    if(result['success']):
        return jsonify(result)
    else:
        return jsonify(result)

@app.route("/modify/<name>")
def modify(name):
    data = {
        'Number': 12,
        'Content':"好棒棒",
        'Note': "眼睛業障重"
    }
    result = DB.modify_data(name,data)
    if(result['success']):
        return jsonify(result)
    else:
        return jsonify(result)

@app.route("/deviceInfo")
def device():
    content = DB.show_device_info()
    try:
        return jsonify(content)
    except TypeError as e:
        return str(content)

@app.route("/login",methods=["POST"])
def login():
    if(request.method == 'POST'):
        account = request.form.get('Account')
        password = request.form.get('Password')
        data = DB.show_data('People')
        for i in data:
            if((data[i]['Account'] == account) and data[i]['Password'] == password):
                return 'Success'
        return 'Failed'
    else:
        '訪問頁面方法錯誤'
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000',debug=True)