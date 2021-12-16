import mysql.connector
from mysql.connector import errors
import mysql_userinfo as us
try :
    # 1. DB 연결
    connection = us.get_connection()

    # 실행한 결과 받아오기 - 딕셔너리
    query = '''select * from test;'''
    cursor = connection.cursor(dictionary = True)
    cursor.execute(query)
    record_list = cursor.fetchall() 
    print(record_list)


    for row in record_list :
        print('id = ', row['id'])
        print('name = ', row['name'])
        print('data = ', row['date'].isoformat())


except errors as e :
    print('Error', e)
finally :
    cursor.close()
    if connection.is_connected() :
        connection.close()
        print('MySQL connectionis closed')
