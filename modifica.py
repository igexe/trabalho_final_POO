from senha import p
from database_conect import db_conect
from consultas import execute_query
from tkinter import *
from tkinter import ttk
from le_dados import read_query as rq
import pandas as pd

def mod():
    janela=Tk()
    janela.title('modifica estoque')


    codigo = Label(janela, text='codigo')
    codigo.grid(row=0, column=0)
    digita_codigo = Entry(janela)
    digita_codigo.grid(row=0, column=1)

    marca = Label(janela, text='marca')
    marca.grid(row=0, column=2)
    digita_marca = Entry(janela)
    digita_marca.grid(row=0, column=3)

    ref=Label(janela,text='referencia')
    ref.grid(row=0,column=4)
    digita_ref=Entry(janela)
    digita_ref.grid(row=0,column=5)

    sexo=Label(janela,text='sexo')
    sexo.grid(row=0,column=6)
    digita_sexo=Entry(janela)
    digita_sexo.grid(row=0,column=7)

    idade=Label(janela,text='idade')
    idade.grid(row=1,column=0)
    digita_idade=Entry(janela)
    digita_idade.grid(row=1,column=1)

    valor=Label(janela,text='valor')
    valor.grid(row=1,column=2)
    digita_valor=Entry(janela)
    digita_valor.grid(row=1,column=3)

    quantidade=Label(janela,text='quantidade')
    quantidade.grid(row=1,column=4)
    digita_quantidade=Entry(janela)
    digita_quantidade.grid(row=1,column=5)

    global busc_cod,busc_marca,busc_ref,busca_sexo,busc_idade,busc_val,busca_quant
    busc_cod=None
    busc_marca=None
    busc_ref=None
    busca_sexo=None
    busc_idade=None
    busc_val=None
    busca_quant=None

    tabela=ttk.Treeview(janela)
    tabela['columns']=('marca','referencia','sexo','idade','valor','quantidade')

    tabela.heading('#0', text='COD')
    tabela.heading('marca',text='MARCA')
    tabela.heading('referencia',text='REF')
    tabela.heading('sexo',text='SEXO')
    tabela.heading('idade',text='IDADE')
    tabela.heading('valor',text='VALOR')
    tabela.heading('quantidade',text='QUANTIDADE')

    tabela.column('#0', width=50)
    tabela.column('marca',width=100)
    tabela.column('referencia',width=75)
    tabela.column('sexo',width=50)
    tabela.column('idade',width=50)
    tabela.column('valor',width=75)
    tabela.column('quantidade',width=100)


    def busca():
        global busc_cod,busc_marca,busc_ref,busca_sexo,busc_idade,busc_val,busca_quant

        tabela.delete(*tabela.get_children())
        
        try:
            int(digita_codigo.get())
            busc_cod=int(digita_codigo.get())

        except ValueError:
            if busc_cod is None:pass
            else:busc_cod=None

        
        if digita_marca.get()=='':
            if busc_marca is None:pass
            else:busc_marca=None

        else:busc_marca=digita_marca.get()


        if digita_ref.get()=='':
            if busc_ref is None:pass
            else:busc_ref=None

        else:busc_ref=digita_ref.get()


        if digita_sexo.get()=='':
            if busca_sexo is None:pass
            else:busca_sexo=None

        else:busca_sexo=digita_sexo.get()


        if digita_idade.get()=='':
            if busc_idade is None:pass
            else:busc_idade=None

        else:busc_idade=digita_idade.get()


        try:
            float(digita_valor.get())
            busc_val=int(digita_valor.get())

        except ValueError:
            if busc_val is None:pass
            else:busc_val=None


        try:
            int(digita_quantidade.get())
            busca_quant=int(digita_quantidade.get())

        except ValueError:
            if busca_quant is None:pass
            else:busca_quant=None


        db=[]
        q='''
        select *
        from sapato;
        '''

        connection=db_conect('localhost','root',p(),'estoque')
        results=rq(connection,q)

        for x in results:
            db.append(x)

        colunas=['codigo','marca','referencia','sexo','idade','valor','quantidade']
        df=pd.DataFrame(db,columns=colunas)
        sapatos=[]

        for index,row in df.iterrows():
            sapatos.append(dict(row.loc[['codigo','marca','referencia','sexo','idade','valor','quantidade']]))


        if busc_cod is None and busc_marca is None and busc_ref is None and busca_sexo is None and busc_idade is None and busc_val is None and busca_quant is None:
            for x in sapatos:
                tabela.insert('','end',text=x['codigo'],values=(x['marca'],x['referencia'],x['sexo'],x['idade'],x['valor'],x['quantidade']))

        else:
            temp=sapatos
            achados=[]
            if busc_cod is not None:
                for x in temp:
                    if x['codigo']==busc_cod:
                        achados.append(x)
                temp=achados
                achados=[]
            else:pass

            if busc_marca is not None:
                for x in temp:
                    if x['marca']==busc_marca:
                        achados.append(x)
                temp=achados
                achados=[]
            else:pass

            if busc_ref is not None:
                for x in temp:
                    if x['referencia']==busc_ref:
                        achados.append(x)
                temp=achados
                achados=[]
            else:pass

            if busca_sexo is not None:
                for x in temp:
                    if x['sexo']==busca_sexo:
                        achados.append(x)
                temp=achados
                achados=[]
            else:pass

            if busc_idade is not None:
                for x in temp:
                    if x['idade']==busc_idade:
                        achados.append(x)
                temp=achados
                achados=[]
            else:pass

            if busc_val is not None:
                for x in temp:
                    if x['valor']==busc_val:
                        achados.append(x)
                temp=achados
                achados=[]
            else:pass

            if busca_quant is not None:
                for x in temp:
                    if x['quantidade']==busca_quant:
                        achados.append(x)
                temp=achados
                achados=[]
            else:pass


            achados=temp
            for x in achados:
                tabela.insert('','end',text=x['codigo'],values=(x['marca'],x['referencia'],x['sexo'],x['idade'],x['valor'],x['quantidade']))


    botao=Button(janela,text='buscar',command=busca)
    botao.grid(row=1,column=7)

    tabela.grid(row=2, column=3, columnspan=2)


    def modifica():

        global codigo,mod_marca,mod_ref,mod_sexo,mod_idade,mod_valor,mod_quantidade

        item_selecionado=tabela.selection()[0]
        codigo=tabela.item(item_selecionado,'text')

        mod_estoque=Tk()
        mod_estoque.title('modifica item')

        l_marca=Label(mod_estoque,text='marca')
        l_marca.grid(row=0,column=0)
        mod_marca=Entry(mod_estoque)
        mod_marca.grid(row=0,column=1)


        l_ref=Label(mod_estoque,text='referencia')
        l_ref.grid(row=0,column=2)
        mod_ref=Entry(mod_estoque)
        mod_ref.grid(row=0,column=3)


        l_sexo=Label(mod_estoque,text='sexo')
        l_sexo.grid(row=0,column=4)
        mod_sexo=Entry(mod_estoque)
        mod_sexo.grid(row=0,column=5)


        l_idade=Label(mod_estoque,text='idade')
        l_idade.grid(row=0,column=6)
        mod_idade=Entry(mod_estoque)
        mod_idade.grid(row=0,column=7)


        l_valor=Label(mod_estoque,text='valor')
        l_valor.grid(row=1,column=2)
        mod_valor=Entry(mod_estoque)
        mod_valor.grid(row=1,column=3)


        l_quantidade=Label(mod_estoque,text='quantidade')
        l_quantidade.grid(row=1,column=4)
        mod_quantidade=Entry(mod_estoque)
        mod_quantidade.grid(row=1,column=5)

        def muda():
            global codigo,mod_marca,mod_ref,mod_sexo,mod_idade,mod_valor,mod_quantidade
            ok=False

            confirma=Label(mod_estoque,text='campos modificados com sucesso',fg='green')

            connection=db_conect('localhost','root',p(),'estoque')

            if mod_marca.get()=='':
                pass
            else:
                up="update sapato set marca='"+str(mod_marca.get())+"' where codigo="+str(codigo)+";"
                execute_query(connection,up)
                ok=True

            if mod_ref.get()=='':
                pass
            else:
                up="update sapato set referencia='"+str(mod_ref.get())+"' where codigo="+str(codigo)+";"
                execute_query(connection,up)
                ok=True

            if mod_sexo.get()=='':
                pass
            else:
                up="update sapato set sexo='"+str(mod_sexo.get())+"' where codigo="+str(codigo)+";"
                execute_query(connection,up)
                ok=True

            if mod_idade.get()=='':
                pass
            else:
                up="update sapato set idade='"+str(mod_idade.get())+"' where codigo="+str(codigo)+";"
                execute_query(connection,up)
                ok=True

            if mod_valor.get()=='':
                pass
            else:
                up="update sapato set valor='"+str(mod_valor.get())+"' where codigo="+str(codigo)+";"
                execute_query(connection,up)
                ok=True

            if mod_quantidade.get()=='':
                pass
            else:
                up="update sapato set quantidade='"+str(mod_quantidade.get())+"' where codigo="+str(codigo)+";"
                execute_query(connection,up)
                ok=True

            if ok==True:
                confirma.grid(row=2,column=3,columnspan=2)

        mod_prod=Button(mod_estoque,text='salvar',command=muda)
        mod_prod.grid(row=3,column=3)


        mod_estoque.mainloop()

    mod_botao=Button(janela,text='modificar',command=modifica)
    mod_botao.grid(row=3,column=3)

    janela.mainloop()
