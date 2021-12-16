import mysql.connector
from mysql.connector import errors
import mysql_userinfo as us
try :
    # 1. DB 연결
    connection = us.user_connect

    name = '김나나'
    data = '2021-12-15'

    # 데이터베이스나 테이블은 꼭 워크벤치에서 만들 것
    # 따옴표 세개는 문자열
    # 2. 쿼리문 만들기
    # 1) query = '''insert into test(name) values('mike');'''
    query ='''insert into test(name, date) values(%s, %s);'''
    # query ='''insert into test(name) values(%s);'''
    # 튜플 만들 때, 데이터가 1개인 경우에는 콤마를 꼭 써준다. 
    record= (name,data) # 튜플
    # 3. 커넥션으로부터 커서를 가져온다.
    cursor = connection.cursor()
    # 4. 쿼리문을 커서에 넣어서 실행한다.
    cursor.execute(query, record)
    # 5. 커넥션을 커밋한다 DB에 영구적으로 반영한다.
    connection.commit()

except errors as e :
    print('Error', e)
finally :
    if connection.is_connected() :
        cursor.close()
        connection.close()
        print('MySQL connectionis closed')
