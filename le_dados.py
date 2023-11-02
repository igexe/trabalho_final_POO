import mysql.connector
from mysql.connector import Error
from database_conect import db_conect
from senha import p
import pandas as pd

def read_query(connection,query):
    cursor=connection.cursor()
    result=None
    try:
        cursor.execute(query)
        result=cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")



# função que le todos os dados da tabela
def read_all():

    #senha
    pw=p()

    #lista que recebera os dados da nossa tabela
    db=[]

    #operação sql para nos retornar nossos dados da tabela sql
    q='''
    select *
    from sapato;
    '''

    #conexão com o banco de dados
    connection=db_conect('localhost','root',pw,'estoque')

    #consulta no banco de dados
    results=read_query(connection,q)

    for x in results:
        db.append(x)

    #criação do dataframe pandas
    colunas=['codigo','marca','referencia','sexo','idade','valor','quantidade']
    df=pd.DataFrame(db,columns=colunas)
    print(df)