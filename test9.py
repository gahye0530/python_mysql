import mysql.connector
from mysql.connector import errors
import mysql_userinfo as us
try :
    # 1. DB 연결
    connection = us.user_connect

    # 2. 쿼리문 만들기
    query = '''delete from test where id = %s;'''
    record= [(2, ), (5, ), (7, )] # 튜플
    # 3. 커넥션으로부터 커서를 가져온다.
    cursor = connection.cursor()
    # 4. 쿼리문을 커서에 넣어서 실행한다.
    cursor.executemany(query, record)
    # 5. 커넥션을 커밋한다 DB에 영구적으로 반영한다.
    connection.commit()

except errors as e :
    print('Error', e)
finally :
    if connection.is_connected() :
        cursor.close()
        connection.close()
        print('MySQL connectionis closed')
