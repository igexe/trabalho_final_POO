from mysql.connector import Error

def execute_query(connection, query):
    cursor=connection.cursor()

    try:
        cursor.execute(query)
        # connection.commit garante que os comandos detalhados em consultas sql sejam implementados
        connection.commit()
        print('Query successful')
    
    except Error as err:
        print(f"Error: '{err}'")