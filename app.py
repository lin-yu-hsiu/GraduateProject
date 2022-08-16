from msilib.schema import Error
import re
from traceback import print_tb
from flask import Flask, redirect,render_template, url_for,request,jsonify
from flask_cors import CORS
import DB,json
import os

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
        return str(e)

@app.route("/create/<name>")
def insert(name):
    data = {
        "UUID": "Test9",
        "Message": "目前所在位置為 B-2",
        "MapNum": 4,
        "Xaxis": 100,  
        "Yaxis": 100,
        "Battery": "100%",
        "Note": "none",
        "Place": '地點8'
    }
    result = DB.insert_data(name,data)
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

@app.route("/deviceInfo/<name>")
def device(name):
    content = DB.show_device_info(name)
    try:
        return jsonify(content)
    except TypeError as e:
        return str(e)

@app.route("/deviceInfo")
def allDevice():
    content = DB.show_device_info(-1)
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

@app.route("/modifyBLE",methods=["POST"])
def modifyBLE():
    data = str(request.data,encoding="UTF-8")
    temp = json.loads(data)
    result = DB.modify_BLE(temp)
    if(result['success']):
        return jsonify(result)
    else:
        return jsonify(result)

@app.route("/switchBLE",methods=["POST"])
def switchBLE():
    data = str(request.data,encoding="UTF-8")
    temp = json.loads(data)
    result = DB.switch_BLE(temp)
    if(result['success']):
        return jsonify(result)
    else:
        return jsonify(result)

@app.route("/deleteBLE",methods=["POST"])
def deleteBLE():
    data = str(request.data,encoding="UTF-8")
    temp = json.loads(data)
    result = DB.delete_data("BLE",temp['UUID'])
    if(result['success']):
        return jsonify(result)
    else:
        return jsonify(result)

@app.route("/createVenue",methods=["POST"])
def createVenue():
    data = str(request.data,encoding="UTF-8")
    temp = json.loads(data)
    result = DB.create_venue(temp['Venue'])
    if(result['success']):
        return jsonify(result)
    else:
        return jsonify(result)

@app.route("/deleteVenue",methods=["POST"])
def deleteVenue():
    data = str(request.data,encoding="UTF-8")
    temp = json.loads(data)
    result = DB.delete_venue(temp['Venue'])
    if(result['success']):
        data = DB.show_data('Map')
        for i in data:
            if(data[i]['Venue'] == temp['Venue']):
                result = DB.delete_data('Map',data[i]['Number'])
                if(not result['success']):
                    return jsonify({'success': 0, 'result': 'Fail to Delete Map Content.'})
        return jsonify({'success': 1, 'result': 'Success to Delete Content.'})
    else:
        return jsonify({'success': 0, 'result':'Fail to Delete Venue'})

@app.route("/insertArea",methods=["POST"])
def insertArea():
    data = str(request.data,encoding="UTF-8")
    temp = json.loads(data)
    basedir = os.path.abspath(os.path.dirname(__file__))
    temp['Route'] = basedir + "\\" + temp['fileName']
    del temp['fileName']
    result = DB.insert_data(temp['Venue'],temp) 
    if(result['success']):
        result = DB.insert_data("Map",temp)
        if(result['success']):
            return jsonify(result)
        else:
            return jsonify(result)
    else:
        return jsonify(result)

@app.route("/deleteArea",methods=["POST"])
def deleteArea():
    data = str(request.data,encoding="UTF-8")
    temp = json.loads(data)
    content = DB.show_data("Map")
    venue = ''
    area = ''
    for i in range(0,len(content)):
        if (content[i]['Number'] == temp['MapNum']):
            venue = content[i]['Venue']
            area = content[i]['Area']
    result = DB.delete_data("Map",temp["MapNum"])
    if(result['success']):
        result = DB.delete_data(venue,area)
        if(result['success']):
            return jsonify(result)
        else:
            return jsonify(result)
    else:
        return jsonify(result)

@app.route("/showVenue")
def showVenue():
    result = DB.show_venue()
    temp = { "場館": result }
    return jsonify(temp)

@app.route("/newDevice",methods=["POST","GET"])
def newDevice():
    data = {}
    if (request.method == 'POST'):
        data = str(request.data,encoding="UTF-8")
        temp = json.loads(data)
        data = { "UUID": temp['UUID'] }
        result = DB.insert_data("BLE", data)
        if(result['success']):
            return jsonify(result)
        else:
            return jsonify(result)
    elif (request.method == 'GET'):
        free = []
        busy = []
        data = DB.show_data('BLE')
        for i in data:
            if (data[i]['MapNum'] == None):
                free.append(data[i]['UUID'])
            else:
                busy.append(data[i]['UUID'])
        data = { "free": free, "busy": busy }
        return jsonify(data)

@app.route("/insertBLE",methods=["POST"])
def insertBLE():
    data = str(request.data,encoding="UTF-8")
    temp = json.loads(data)
    data = DB.show_data('Map')
    MapNum = -1
    for i in data:
        if (data[i]['Venue'] == temp['Venue'] and data[i]['Area'] == temp['Area']):
            MapNum = data[i]['Number']
            break
    del temp['Venue']
    del temp['Area']
    temp['MapNum'] = MapNum
    result = DB.modify_BLE(temp)
    if(result['success']):
        return jsonify(result)
    else:
        return jsonify(result)

@app.route("/uploadPic",methods=["POST"])
def uploadPic():
    try:
        basedir = os.path.abspath(os.path.dirname(__file__))
        targetdir = os.path.join(basedir,'public\\images')
        exist = os.path.exists(targetdir)
        if(exist == False):
            os.mkdir(targetdir)
        img = request.files.get('file')
        format = img.filename[img.filename.index('.'):]
        if format in ('.jpg','.png','.jpeg','.HEIC','.jfif','.gif'):
            dir = targetdir + '\\' + img.filename.replace(format,'.jpg')
            img.save(dir)
            result = {'success': 1, 'result': 'Upload Successfully'}
        else:
            result = {'success': 0, 'result': 'Type Wrong'}

    except Exception as e:
        print(str(e))
        result = {'success': 0, 'result': 'Upload Failed'}
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000',debug=True)