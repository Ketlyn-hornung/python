#conta.py

class Conta:

    #numero
    #titular
    #saldo
    #limite
    #construtor de classe
    def __init__(self,numero,titular,saldo,limite):
        print('construindo objeto...{}'.format(self))
        #atributos privado
        self.__numero=numero
        self.__titular=titular
        self.__saldo=saldo
        self.__limite=limite

    def depositar(self,valor):
        self.__saldo+=valor

    def sacar(self,valor):
        if(self.__saldo+self.__limite>=valor):
            self.__saldo-=valor
            return True
        
        else:
                print('nao ha saldo suficiente para sacar')
                return False
            
        

    def transferir(self,valor,destino):
        if self.sacar(valor):
           destino.depositar(valor)
        else:
               print('nao ha saldo para transferencia')
            
               
    @property
    def numero(self):
     return self.__numero
           
    @property
    def titular(self):
     return self.__titular
        
    @property
    def saldo(self):
     return self.__saldo

           
    @property
    def limite(self):
     return self.__limite

    @limite.setter
    def limite(self,limite):
        self.__limite=limite

    #exemplo de metodo estatico
    @staticmethod
    def codigo_banco():
        return '001'

Contajoao=Conta(123,'joao da silva', 100,1000)
Contaze=Conta(456,'jose da silva',100,1000)

Contajoao.transferir(500,Contaze)
Contaze.limite = 1000
print(Conta.codigo_banco())
