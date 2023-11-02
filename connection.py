import mysql.connector
from mysql.connector import Error

# o metodo server_connection faz a ligação com o servidor sql
def server_connection(host_name,user_name,user_pass):
    connection=None
    try:
        connection=mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_pass,
        )
        # caso a conexão seja bem sucedida retorna a menssagem a baixo
        print('MySQL Database connection sucessful')
    except Error as err:
        #caso a conexão falhe é retornada a menssagem de erro reportando o erro
        print(f"Error: '{err}'")

    return connection