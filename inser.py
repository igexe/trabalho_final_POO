from database_conect import db_conect
from consultas import execute_query
from senha import p
from tkinter import *

def insere():

    # cria a janela para cadastro de produtos
    janela=Tk()
    # mudando titulo da janela
    janela.title('cadastro')


    marca=Label(janela,text='marca')
    marca.grid(row=0,column=0)
    digita_marca=Entry(janela)
    digita_marca.grid(row=0,column=1)
    global marca_err
    marca_err=None

    ref=Label(janela,text='referencia')
    ref.grid(row=0,column=2)
    digita_ref=Entry(janela)
    digita_ref.grid(row=0,column=3)
    global ref_err
    ref_err=None

    sexo=Label(janela,text='sexo')
    sexo.grid(row=0,column=4)
    digita_sexo=Entry(janela)
    digita_sexo.grid(row=0,column=5)
    global sexo_err
    sexo_err=None

    idade=Label(janela,text='idade')
    idade.grid(row=0,column=6)
    digita_idade=Entry(janela)
    digita_idade.grid(row=0,column=7)
    global idade_err
    idade_err=None

    valor=Label(janela,text='valor')
    valor.grid(row=1,column=2)
    digita_valor=Entry(janela)
    digita_valor.grid(row=1,column=3)
    global valor_err
    valor_err=None

    quantidade=Label(janela,text='quantidade')
    quantidade.grid(row=1,column=4)
    digita_quantidade=Entry(janela)
    digita_quantidade.grid(row=1,column=5)
    global quantidade_err
    quantidade_err=None

    # esta função que sera chamada no botão Cadastra criado posteriormente serve para verificar se todos os campos estão corretamente preenchidos para não haver nenhum erro no sql
    def verifica():
        global marca_err
        global ref_err
        global sexo_err
        global idade_err
        global valor_err
        global quantidade_err

        if digita_marca.get()=='':
            if marca_err is None:
                marca_err=Label(janela,text='O campo marca não pode ser vazio',fg='red')
                marca_err.grid(row=2,column=2,columnspan=3)
            else:pass

        else:
            if marca_err is None:pass
            else:
                marca_err.grid_forget()
                marca_err=None


        if digita_ref.get()=='':
            if ref_err is None:
                ref_err=Label(janela,text='O campo referencia não pode ser vazio',fg='red')
                ref_err.grid(row=3,column=2,columnspan=3)
            else:pass
            
        else:
            if ref_err is None:pass
            else:
                ref_err.grid_forget()
                ref_err=None


        if len(digita_sexo.get())>4:
            if sexo_err is None:
                sexo_err=Label(janela,text='O campo sexo deve ter no maximo 3 caracteres',fg='red')
                sexo_err.grid(row=4,column=2,columnspan=3)
            else:pass

        else:
            if sexo_err is None:pass
            else:
                sexo_err.grid_forget()
                sexo_err=None


        if digita_idade.get()=='':
            if idade_err is None:
                idade_err=Label(janela,text='O campo idade não pode ser vazio',fg='red')
                idade_err.grid(row=5,column=2,columnspan=3)
            else:pass

        elif len(digita_idade.get())>3:
            if idade_err is None:
                idade_err=Label(janela,text='O campo idade deve ter no maximo 3 caracteres',fg='red')
                idade_err.grid(row=5,column=2,columnspan=3)
            else:pass
 
        else:
            if idade_err is None:pass
            else:
                idade_err.grid_forget()
                idade_err=None


        try:
            float(digita_valor.get())
            if valor_err is None:pass
            else:
                valor_err.grid_forget()
                valor_err=None
        
        except ValueError:
            if valor_err is None:
                valor_err=Label(janela,text='Erro no campo valor o campo não pode ser vazio e tente digitar o valor com "." ao invez de ","',fg='red')
                valor_err.grid(row=6,column=1,columnspan=6)
            else:pass


        try:
            int(digita_quantidade.get())
            if quantidade_err is None:pass
            else:
                quantidade_err.grid_forget()
                quantidade_err=None

        except ValueError:
            if quantidade_err is None:
                quantidade_err=Label(janela,text='Erro no campo quantidade o campo não pode ser vazio e deve ser um numero inteiro',fg='red')
                quantidade_err.grid(row=7,column=1,columnspan=6)
            else:pass


        if marca_err is None and ref_err is None and sexo_err is None and idade_err is None and valor_err is None and quantidade_err is None:
            if digita_sexo.get()=='':
                insert="insert into sapato(marca,referencia,idade,valor,quantidade) values('"+str(digita_marca.get())+"','"+str(digita_ref.get())+"','"+str(digita_idade.get())+"',"+str(digita_valor.get())+","+str(digita_quantidade.get())+");"
                connection=db_conect('localhost','root',p(),'estoque')
                execute_query(connection,insert)
                sucesso=Label(janela,text='Cadastro realizado com sucesso',fg='green')
                sucesso.grid(row=2,column=3,columnspan=3)
                digita_marca.delete(0,END)
                digita_ref.delete(0,END)
                digita_idade.delete(0,END)
                digita_valor.delete(0,END)
                digita_quantidade.delete(0,END)



            else:
                insert="insert into sapato(marca,referencia,sexo,idade,valor,quantidade) values('"+str(digita_marca.get())+"','"+str(digita_ref.get())+"','"+str(digita_sexo.get())+"','"+str(digita_idade.get())+"',"+str(digita_valor.get())+","+str(digita_quantidade.get())+");"
                connection=db_conect('localhost','root',p(),'estoque')
                execute_query(connection,insert)
                sucesso=Label(janela,text='Cadastro realizado com sucesso',fg='green')
                sucesso.grid(row=2,column=3,columnspan=3)
                digita_marca.delete(0,END)
                digita_ref.delete(0,END)
                digita_sexo.delete(0,END)
                digita_idade.delete(0,END)
                digita_valor.delete(0,END)
                digita_quantidade.delete(0,END)


        else:pass

    # botão para concluir o cadastro do produto casso todos os campos estejão corretamente preechidos
    cadastra=Button(janela,text='Cadastra',command=verifica)
    cadastra.grid(row=10,column=3)

    janela.mainloop()