from unittest import result
from urllib import response
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
        "UUID": "Test2",
        "Message": "鼎元我大哥",
        "MapNum": 2,
        "Xaxis": 100,
        "Yaxis": 100,
        "Battery": "50%",
        "Status": 0,
        "Note": "none"
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

@app.route("/test",methods=["POST"])
def test():
    data = str(request.data,encoding="UTF-8")
    temp = json.loads(data)
    print(temp)
    result = DB.modify_BLE(temp)
    # if(result['success']):
    #     return jsonify(result)
    # else:
    #     return jsonify(result)
    return 'Success'

    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000',debug=True)