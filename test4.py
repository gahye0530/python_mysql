import mysql.connector
from mysql.connector import errors
import mysql_userinfo as us
try :
    # 1. DB 연결
    connection = us.user_connect

    # 실행한 결과 받아오기 - 리스트
    query = '''select * from test where id = %s;'''
    param = (3, )
    cursor = connection.cursor()
    cursor.execute(query, param)
    record_list = cursor.fetchall() 
    print(record_list)

    for row in record_list :
        print('id = ', row[0])
        print('name = ', row[1])
        # print('data = ', row[2].isoformat())
        print('data = ', row[2].weekday())


except errors as e :
    print('Error', e)
finally :
    cursor.close()
    if connection.is_connected() :
        connection.close()
        print('MySQL connectionis closed')
