import sqlite3

dbContent = {
    'People': ['Email','Account','Password'],
    'BLE':['UUID','MessageNum','MapNum','Xaxis','Yaxis','Battery','Status'],
    'Message':['Number','Content','Note'],
    'Map':['Number','Route'],
    'PK':{
        'People':'Email',
        'BLE':'UUID',
        'Message':'Number',
        'Map':'Number'
    }
}

def show_data(table_name):                  #回傳表格內容
    conn = sqlite3.connect('test.db', check_same_thread=False)
    cursor = conn.cursor()
    try:
        cursor.execute('Select * from {}'.format(table_name))
        conn.commit()
        records = cursor.fetchall()
        cursor.close()
        conn.close()
        result = {}
        for row in range(0,len(records)):
            temp = {}
            for col in range(0, len(records[row])):
                temp[dbContent[table_name][col]] = records[row][col]
            result[row] = temp
        return result
    except sqlite3.OperationalError as e:
        return e

#新增一筆資料 (BLE 資料中的電量和狀態預設為 "0%" 和 "Turn Off"), (Map 和 Message 的 PK 有 AUTOINCREMENT)
def insert_data(table_name, content):       
    conn = sqlite3.connect('test.db', check_same_thread=False)
    cursor = conn.cursor()
    try:
        ins = 'Insert into {} ('.format(table_name)
        if(table_name == 'People'):
            ins += 'Email,Account,Password) values ('
        elif(table_name == 'BLE'):
            ins += 'UUID,MessageNum,MapNum,Xaxis,Yaxis) values ('
        elif(table_name == 'Message'):
            ins += 'Content,Note) values ('
        elif(table_name == 'Map'):
            ins += 'Route) values ('
        for i in content:
            if(type(content[i] == str)):
                ins += str("'{}',".format(content[i]))
            else:
                ins += str(str(content[i]) + ',')
        ins = ins[:-1] + ');'
        cursor.execute(ins)
        conn.commit()
        cursor.close()
        conn.close()
        return {"success": 1,'Result': '新增成功'}
    except sqlite3.OperationalError as e:
        return {"success": 0, "Result": e}

def delete_data(table_name, pk):        #刪除一筆資料
    conn = sqlite3.connect('test.db', check_same_thread=False)
    cursor = conn.cursor()
    try:
        ins = 'Delete from {} where {} = {};'.format(table_name,dbContent['PK'][table_name],pk)
        cursor.execute(ins)
        conn.commit()
        cursor.close()
        conn.close()
        return {"success": 1,'Result': '刪除成功'}
    except sqlite3.OperationalError as e:
        return {"success": 0, "Result": e}

def delete_all(table_name):
    conn = sqlite3.connect('test.db', check_same_thread=False)
    cursor = conn.cursor()
    try:
        ins = 'Delete from {};'.format(table_name)
        cursor.execute(ins)
        conn.commit()
        cursor.close()
        conn.close()
        return {"success": 1,'Result': '刪除成功'}
    except sqlite3.OperationalError as e:
        return {"success": 0, "Result": e}

def modify_data(table_name,content):        #修正表格資料 (BLE 資訊中的電量以及狀態將在其他路由處理)
    conn = sqlite3.connect('test.db', check_same_thread=False)
    cursor = conn.cursor()
    try:
        ins = 'Update {} set '.format(table_name)
        if(table_name == 'People'):
            ins += 'Account = "{}",Password = "{}" where Email = "{}";'\
                .format(content['Account'],content['Password'],dbContent['PK']['People'],content['Email'])
        elif(table_name == 'BLE'):
            ins += 'MessageNum = {},MapNum = {},Xaxis = {},Yaxis = {} where UUID = "{}";'\
                .format(content['MessageNum'],content['MapNum'],content['Xaxis'],content['Yaxis'],content['UUID'])
        elif(table_name == 'Message'):
            ins += 'Content = "{}",Note = "{}" where Number = {};'\
                .format(content['Content'],content['Note'],content['Number'])
        elif(table_name == 'Map'):
            ins += 'Route = {} where Number = {};'\
                .format(content['route'],content['Number'])
        cursor.execute(ins)
        conn.commit()
        cursor.close()
        conn.close()
        return {"success": 1,'Result': '修改成功'}
    except sqlite3.OperationalError as e:
        return {"success": 0, "Result": e}

data = {
        'Number': 12,
        'Content':"紫紅好棒棒",
        'Note': "眼睛業障重"
    }
# print(modify_data('Message',data))