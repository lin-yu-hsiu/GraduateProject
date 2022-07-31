"""
注意事項:
    1. 資料中請不要使用 ' 會影響 sql 語法
    2. 之後記得部分改成 POST (鈺修進度)

路由內容:
    ★ /table/<表格名稱> => 查看目標表格內容 => GET 
    ★ /deviceInfo => 查看所有裝置狀態 => GET
    ★ /deviceInfo/<館>
    ★ /createVenue => 新增場館 => POST (備註1)
    ★ /deleteVenue => 刪除場館 => POST (備註2)
    ★ /login => 登入檢查 => POST (備註2)
    ★ /modifyBLE => 修正BLE內部內容  => POST (備註3)
    ★ /switchBLE => 一鍵開關 => POST (備註4)
    ★ /deleteBLE => 刪除特定 BLE => POST (備註5)
    ★ /deleteAll/<表格名稱> => 刪除該表格所有資料 => GET
    ★ /insertArea => 新增區域 => POST(備註6)
    ★ /deleteArea => 刪除區域 => POST(備註7)

備註:
    1. 以 json 來 POST, 傳入場館名稱
    2. 以 json 來 POST, 傳入場館名稱
    2. 以 value 來 POST, 分別傳入帳號密碼
    3. 以 json 來 POST, 傳入 UUID, Message, Status, Note
    4. 以 json 來 POST, 傳入 Status
    5. 以 json 來 POST, 傳入 UUID
    6. 以 json 來 POST, 傳入 Route, Venue, Area
    7. 以 json  來 POST, 傳入 MapNum
"""
import sqlite3
dbContent = {
    'People': ['Email','Account','Password'],
    'BLE':['UUID','Message','MapNum','Xaxis','Yaxis','Battery','Status','Note','Place'],
    'Map':['Number','Route','Venue','Area'],
    '場館內容':['Route','Venue','Area'],
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
                if(table_name == 'BLE' or table_name == 'People' or table_name == 'Map'):
                    temp[dbContent[table_name][col]] = records[row][col]
                else:
                    temp[dbContent['場館內容'][col]] = records[row][col]
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
            ins += 'UUID,Message,MapNum,Xaxis,Yaxis,Battery,Status,Note,Place) values ('
        else:
            ins += 'Route,Venue,Area) values ('
        for i in content:
            if(type(content[i]) == str):
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
        return {"success": 0, "Result": str(e)}

def delete_data(table_name, pk):        #刪除一筆資料
    conn = sqlite3.connect('test.db', check_same_thread=False)
    cursor = conn.cursor()
    try:
        if(table_name == 'BLE' or table_name == 'People' or table_name == 'Map'):
            ins = 'Delete from {} where {} = '.format(table_name,dbContent['PK'][table_name])
        else:
            ins = 'Delete from {} where Area = '.format(table_name)
        if(type(pk) == str):
            ins += "'{}';".format(pk)
        else:
            ins += '{};'.format(pk)
        cursor.execute(ins)
        conn.commit()
        cursor.close()
        conn.close()
        return {"success": 1,'Result': '刪除成功'}
    except sqlite3.OperationalError as e:
        return {"success": 0, "Result": str(e)}

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
        return {"success": 0, "Result": str(e)}

def modify_BLE(content):        #修正表格資料 (BLE 資訊中的電量以及狀態將在其他路由處理)
    conn = sqlite3.connect('test.db', check_same_thread=False)
    cursor = conn.cursor()
    try:
        ins = "Update BLE set "
        for i in content:
            if(i != 'UUID'):
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
        return {"success": 0, "Result": str(e)}

def modify_battery(content):            #針對 BLE 之中的電量進行修正
    conn = sqlite3.connect('test.db', check_same_thread=False)
    cursor = conn.cursor()
    try:
        ins = 'Update BLE set '
        ins += 'Battery = {} where UUID = "{}";'.format(content['Status'],content['UUID'])
        cursor.execute(ins)
        conn.commit()
        cursor.close()
        conn.close()
        return {"success": 1,'Result': '修改成功'}
    except sqlite3.OperationalError as e:
        return {"success": 0, "Result": str(e)}

def show_device_info(number):
    conn = sqlite3.connect('test.db', check_same_thread=False)
    cursor = conn.cursor()
    try:
        if(number != -1):
            cursor.execute('SELECT * from BLE INNER JOIN Map on BLE.MapNum = Map.Number where BLE.MapNum = {};'.format(number))
        else:
            cursor.execute('SELECT * from BLE INNER JOIN Map on BLE.MapNum = Map.Number;')
        conn.commit()
        records = cursor.fetchall()
        cursor.close()
        conn.close()
        result = []
        for row in range(0,len(records)):
            temp = {}
            temp['UUID'] = records[row][0]
            temp['Message'] = records[row][1]
            temp['MapNum'] = records[row][2]
            temp['Xaxis'] = records[row][3]
            temp['Yaxis'] = records[row][4]
            temp['Battery'] = records[row][5]
            temp['Status'] = bool(records[row][6])
            temp['Note'] = records[row][7]
            temp['Place'] = records[row][8]
            temp['Route'] = records[row][10]
            temp['Venue'] = records[row][11]
            temp['Area'] = records[row][12]
            result.append(temp)
        return result
    except sqlite3.OperationalError as e:
        return e

def switch_BLE(content):
    conn = sqlite3.connect('test.db', check_same_thread=False)
    cursor = conn.cursor()
    try:
        ins = 'Update BLE set '
        ins += 'Status = {} where MapNum = "{}";'.format(content['Status'],content['MapNum'])
        cursor.execute(ins)
        conn.commit()
        cursor.close()
        conn.close()
        return {"success": 1,'Result': '修改成功'}
    except sqlite3.OperationalError as e:
        return {"success": 0, "Result": str(e)}

def show_venue():
    conn = sqlite3.connect('test.db', check_same_thread=False)
    cursor = conn.cursor()
    try:
        result = []
        cursor.execute('Select * from sqlite_master;')
        conn.commit()
        records = cursor.fetchall()
        for i in range(0,len(records)):
            if(records[i][0] == 'index'):
                continue
            if(records[i][1] == 'People' or records[i][1] == 'Map' or records[i][1] == 'BLE' or records[i][1] == 'sqlite_sequence'):
                continue
            result.append(records[i][1])
        cursor.close()
        conn.close()
        return result
    except sqlite3.OperationalError as e:
        return e

def create_venue(name):
    conn = sqlite3.connect('test.db', check_same_thread=False)
    cursor = conn.cursor()
    try:
        ins = "Create Table '{}' ('Route' TEXT UNIQUE, 'Venue' TEXT, 'Area' TEXT UNIQUE, PRIMARY KEY('Area'));".format(name)
        cursor.execute(ins)
        conn.commit()
        cursor.close()
        conn.close()
        return {"success": 1,'Result': '新增成功'}
    except sqlite3.OperationalError as e:
        return {"success": 0, "Result": str(e)}

def delete_venue(name):
    conn = sqlite3.connect('test.db', check_same_thread=False)
    cursor = conn.cursor()
    try:
        ins = "Drop Table {};".format(name)
        cursor.execute(ins)
        conn.commit()
        cursor.close()
        conn.close()
        return {"success": 1,'Result': '刪除成功'}
    except sqlite3.OperationalError as e:
        return {"success": 0, "Result": str(e)}
