#Arquivo_CSV.py


#permite ler e gravar arquivos .csv do Excel
import csv

#gravando um arquivo .CSV
def gravar():
    tabela=(('PRODUTO','UNIDADE','PREÇO UNITARIO','QUANTIDADE ESTOQUE','VALOR TOTAL'),
            ('Açucar', '2KG', 3,59, 10, 35.90),
            ('Biscoito', '200 Gr', 1.19, 10, 11.90)
            )
    #a objeto de escrita
    saida= csv.writer(open('tabela.csv', 'w', newline=''), delimiter=';')

    #escreve tuplas no arquivo
    saida.writerows(tabela)

#lendo arquivo. csv
def ler():
    tabela=csv.reader(open('tabela.csv'))

 #para cada registro do arquivo,imprima
    for lista in tabela:
        print(lista[0].split(';')[4])

if(__name__ == '__main__'):
   #gravar()
   ler()
    
 
