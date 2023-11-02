from connection import server_connection as server
import pandas as pd
from database import create_database as database
from senha import p
from database_conect import db_conect
from consultas import execute_query
from inser import insere
from le_dados import read_all
from tkinter import *

# para a execução dos codigos a seguir são necessarios o mysql e fazer a instalação das bibliotecas MySQL Connector com o seguinte comando pip install mysql-connector-python e a biblioteca pandas com o seguinte comando pip install pandas


# as partes do codigo que estão identados e comentados são de unica utilização uma vez utilizados não podem ser mais deixados no codigo


    # # pw se refere a senha da nossa conexão sql
    # pw=p()

    # # criando uma conexão com o sql
    # connection=server('localhost','root',pw)

    # # criando um database na nossa conexão
    # query='create database estoque'
    # cria_database=database(connection,query)


    # # criando a tabela sapatos para salvar nossos produtos cadastrados
    # cria_tabela='''
    # create table sapato(
    #     codigo int auto_increment primary key,
    #     marca varchar(40) not null,
    #     referencia varchar(40) not null,
    #     sexo varchar(4),
    #     idade varchar(3) not null,
    #     valor double(4,2) not null,
    #     quantidade int not null
    # );
    # '''
    # # conectando ao database
    # connection=db_conect('localhost','root',pw,'estoque')

    # # criando a tabela dentro do database
    # execute_query(connection,cria_tabela)


# pw=p()

# connection=db_conect('localhost','root',pw,'estoque')

# up= """
# update sapato
# set referencia = 'novo'
# where codigo=1;
# """

# execute_query(connection,up)

# insere()

# read_all()


# codigo para fazer a tela



janela=Tk()
x=''
# mudando titulo da janela
janela.title('estoque')


marca=Label(janela,text='marca')
marca.grid(row=0,column=0)


digita_marca=Entry(janela)
digita_marca.grid(row=0,column=1)

def i():
    x=digita_marca.get()
    print(x)

botao=Button(janela,text='imprime',command=i)
botao.grid(row=1,column=0)

janela.mainloop()