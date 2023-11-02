from database_conect import db_conect
from consultas import execute_query
from senha import p


def insere():
    pw=p()
    marca=input('\ndigite a marca do sapato\n')
    ref=input('\ndigite a referencia do sapato\n')
    sexo=input('\ndigite fem para feminino e masc para masculino\n')
    idade=input('\ndigite inf para sapatos infantis e adt para sapatos adultos\n')
    valor=float(input('\ndigite o valor do sapato\n'))
    quantidade=int(input('\ndigite a quantidade de sapatos dessa referencia\n'))

    insert=insert="insert into sapato(marca,referencia,sexo,idade,valor,quantidade) values ('"+str(marca)+"','"+str(ref)+"','"+str(sexo)+"','"+str(idade)+"',"+str(valor)+","+str(quantidade)+");"


    connection=db_conect('localhost','root',pw,'estoque')
    execute_query(connection,insert)
