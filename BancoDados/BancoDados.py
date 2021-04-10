#Importação de bibliotecas
import sqlite3
from sqlite3 import Error
import os

#Criação da variável para o caminho dinâmico
pastaApp=os.path.dirname(__file__)
nomeBanco=pastaApp+"\\Anamnese.db"

#Função de conexão
def ConexaoBanco():
    con=None
    try:
        con=sqlite3.connect(nomeBanco)
    except Error as ex:
        print(ex)
    return con

#Função query
def dql(query): #select
    vcon=ConexaoBanco()
    c=vcon.cursor()
    c.execute(query)
    res=c.fetchall()
    vcon.close()
    return res

def dml(query): #insert, update, delete
    try:
        vcon = ConexaoBanco()
        c = vcon.cursor()
        c.execute(query)
        vcon.commit()
        vcon.close()
    except Error as ex:
        print(ex)
