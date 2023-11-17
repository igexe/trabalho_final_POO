from mysql.connector import Error

# metodo para a criação de um database
# query se trata do database que estamos criando
# connection é nossa conexão com o sql
def create_database(connection,query):
    
    # cursor se refere a nossa conexão
    cursor=connection.cursor()
    
    try:
        cursor.execute(query)
        print('Database create sucessfully')
    
    except Error as err:
        print(f"Error: '{err}'")