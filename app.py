from unittest import result
from flask import Flask, redirect,render_template, url_for,request,jsonify
from jinja2 import Undefined
import DB,json

app = Flask(__name__)

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

@app.route("/renew_battery",methods = ['POST'])
def renew():
    data = request.data
    data = '100%'
    result = DB.renewBattery(data)
    if(result['success']):
        return 'Success'
    else:
        return 'Failed'


if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000',debug=True)