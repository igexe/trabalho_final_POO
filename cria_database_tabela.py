def cria():
    from connection import server_connection as server
    from senha import p
    from database import create_database as database
    from database_conect import db_conect
    from consultas import execute_query

# para a execução dos codigos a seguir são necessarios o mysql e fazer a instalação das bibliotecas MySQL Connector com o seguinte comando pip install mysql-connector-python a biblioteca pandas com o seguinte comando pip install pandas e a biblioteca pandastable com o comando pip install pandastable

    # criando uma conexão com o sql a função p() chamada em connection se refere a senha da conexão localhost no sql
    connection=server('localhost','root',p())

    # criando um database na nossa conexão
    query='create database estoque'
    cria_database=database(connection,query)


    # criando a tabela sapatos para salvar nossos produtos cadastrados
    cria_tabela='''
    create table sapato(
        codigo int auto_increment primary key,
        marca varchar(40) not null,
        referencia varchar(40) not null,
        sexo varchar(4),
        idade varchar(3) not null,
        valor double(4,2) not null,
        quantidade int not null
    );
    '''
    # conectando ao database
    connection=db_conect('localhost','root',p(),'estoque')

    # criando a tabela dentro do database
    execute_query(connection,cria_tabela)