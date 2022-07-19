"""
注意事項:
    1. 資料中請不要使用 ' 會影響 sql 語法
    2. 之後記得部分改成 POST (鈺修進度)
"""
import sqlite3
dbContent = {
    'People': ['Email','Account','Password'],
    'BLE':['UUID','Message','MapNum','Xaxis','Yaxis','Battery','Status','Note'],
    'Map':['Number','Route','Venue','Area'],
    'PK':{
        'People':'Email',
        'BLE':'UUID',
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
            ins += 'UUID,Message,MapNum,Xaxis,Yaxis,Battery,Status,Note) values ('
        elif(table_name == 'Map'):
            ins += 'Route,Venue,Area) values ('
        for i in content:
            if(type(content[i]) == str):
                ins += str("'{}',".format(content[i]))
            else:
                ins += str(str(content[i]) + ',')
        ins = ins[:-1] + ');'
        print(ins)
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

def modify_BLE(content):        #修正表格資料 (BLE 資訊中的電量以及狀態將在其他路由處理)
    conn = sqlite3.connect('test.db', check_same_thread=False)
    cursor = conn.cursor()
    try:
        ins = "Update BLE set "
        for i in content:
            if(i != 'UUID' and i != 'Place'):
                ins += '{} = '.format(i)
                if(type(content[i]) == str):
                    ins += "'{}'".format(content[i])
                else:
                    ins += '{}'.format(content[i])
                ins += ','
            else:
                continue
        ins = ins[0:len(ins)-1]
        ins += " where UUID = '{}';".format(content['UUID'])
        cursor.execute(ins)
        conn.commit()
        cursor.close()
        conn.close()
        return {"success": 1,'Result': '修改成功'}
    except sqlite3.OperationalError as e:
        return {"success": 0, "Result": e}

def modify_battery(content):            #針對 BLE 之中的電量進行修正
    conn = sqlite3.connect('test.db', check_same_thread=False)
    cursor = conn.cursor()
    try:
        ins = 'Update BLE set '
        ins += 'Battery = {} where UUID = "{}";'.format(content)
        cursor.execute(ins)
        conn.commit()
        cursor.close()
        conn.close()
        return {"success": 1,'Result': '修改成功'}
    except sqlite3.OperationalError as e:
        return {"success": 0, "Result": e}

def show_device_info():
    conn = sqlite3.connect('test.db', check_same_thread=False)
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT * from BLE INNER JOIN Map on BLE.MapNum = Map.Number;')
        conn.commit()
        records = cursor.fetchall()
        cursor.close()
        conn.close()
        result = []
        print(records)
        for row in range(0,len(records)):
            temp = {}
            temp['UUID'] = records[row][0]
            temp['MapNum'] = records[row][1]
            temp['Xaxis'] = records[row][2]
            temp['Yaxis'] = records[row][3]
            temp['Battery'] = records[row][4]
            if(records[row][5] == 1):
                temp['Status'] = True
            else:
                temp['Status'] = False
            temp['Content'] = records[row][6]
            temp['Note'] = records[row][7]
            temp['Route'] = records[row][9]
            temp['Venue'] = records[row][10]
            temp['Area'] = records[row][11]
            result.append(temp)
        return result
    except sqlite3.OperationalError as e:
        return e