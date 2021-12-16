import mysql.connector
from mysql.connector.errors import Error
import mysql_userinfo as us

try :
    connection = us.user_connect


    if connection.is_connected() : 
        db_info = connection.get_server_info()
        print('MySQL info', db_info)

except Error as e :
    print('Error while connecting to MYSQL', e)

finally :
    print('finally')
    if connection.is_connected() :
        connection.close()
        print('MySQL connection is closed')
    else :
        print('connection does not exist')