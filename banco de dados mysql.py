#banco_dados.py
#python -m pip install --upgrade pip
#cd scripts
#pip3 install PyMySQL

#criar banco escola.db usando sqlitestudio

import pymysql

def listaDatabases():
    # executa um comando sql
    cursor.execute('show database')

    #recupera o resultado
    recordset = cursor.fetchall()  #fetch = buscar

    #mostra o resultado

    for registro in recordset:
        print(record)

if(__name__== ' __main__'):
   #cria conexao com o banco
   conexao = pymysql.connect(db='escola.db')
   #cria um cursor
   cursor = conexao.cursor()
   listaDatabase()
