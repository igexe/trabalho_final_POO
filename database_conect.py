import mysql.connector
from mysql.connector import Error

def db_conect(host_name,user_name,user_password,db_name):
    connection=None
    try:
        connection=mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        print('MySQL Database connection successful')
    
    except Error as err:
        print(f"Error: '{err}'")

    return connection