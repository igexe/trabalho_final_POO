from inser import *
from le_dados import *
from cria_database_tabela import *
from modifica import *
from tkinter import *

# a função cria é utilizada para fazer a criação do database e da tabela necessaria porem só pode ser utilizada uma vez pois nas outras vezes onde executado ocorre um erro
# cria()

janela=Tk()
janela.title('menu')

inserir=Button(janela,text='inserir',command=insere)
inserir.grid(row=0,column=0)

busca=Button(janela,text='busca',command=read_all)
busca.grid(row=1,column=0)

modifica=Button(janela,text='modifica',command=mod)
modifica.grid(row=2,column=0)

janela.mainloop()