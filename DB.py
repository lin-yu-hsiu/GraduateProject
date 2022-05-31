import sqlite3
import json

from certifi import contents
dbContent = {
    'User': ['Number','Name','Gender','Mail','Extra']
}

def show_data(table_name):
    conn = sqlite3.connect('test.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('Select * from {}'.format(table_name))
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
