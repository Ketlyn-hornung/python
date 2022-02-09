#arquivo_texto.py

#modo para leitura e gravaçao de arquivos:'r','w','a'
#r = read = somente leitura
#w = write = escrita(perde o que ja tem no arquivo)
#a = append = anexa dados ( nao perde )

# tipos de arquivos: texto ou binario

lista=[]


def entrada():
    quant = int(input('quantas frutas voce quer digitar?'))
    for x in range(1,quant+1):
        fruta=input('Digita a fruta {}:'.format(x))
        lista.append(fruta)

    print(lista)

def gravar():
    arquivo=open('frutas.txt','w')

    for fruta in lista:
     arquivo.write(fruta+'\n')

    arquivo.close()



def ler():
    arquivo=open('frutas.txt','r')
    for linha in arquivo:
     print(linha)
     
     arquivo.close()

     
def anexar():
    arquivo:open('frutas.txt','a')
    for fruta in lista:
        arquivo.write(fruta+'\n')

    arquivo.close()

if(__name__=='__main__'):
   entrada()
   # gravar()
   #ler()
   anexar()
