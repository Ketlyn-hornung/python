Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> lista =[]
>>> lista =["gol","celta","corsa","fiesta","fox"]
>>> lista
['gol', 'celta', 'corsa', 'fiesta', 'fox']
>>> lista=[]
>>> flores=["rosa","orquidea","margarida","tulipa"]
>>> flores
['rosa', 'orquidea', 'margarida', 'tulipa']
>>> filmes=[]
>>> filmes=["matrix","harry potter","panico"]
>>> filmes
['matrix', 'harry potter', 'panico']
>>> raças de gatos=[]
SyntaxError: invalid syntax
>>> raça gatos=[]
SyntaxError: invalid syntax
>>> gatos=[]
>>> gatos=["persa","maine coon","siames","ragdoll","sphynx"]
>>> gatos
['persa', 'maine coon', 'siames', 'ragdoll', 'sphynx']
>>> gatos [3]
'ragdoll'
>>> flores [3]
'tulipa'
>>> flores[0]="violeta"
>>> flores
['violeta', 'orquidea', 'margarida', 'tulipa']
>>> filmes[2]="sexta feira 13"
>>> filmes
['matrix', 'harry potter', 'sexta feira 13']
>>> for filme in filmes:
	print(filme)

	
matrix
harry potter
sexta feira 13
>>> for gatos in gatos:
	print(gatos)

	
persa
maine coon
siames
ragdoll
sphynx
>>> for x in gatos:
	print(x)

	
s
p
h
y
n
x
>>> gatos
'sphynx'
>>> gatos=["persa","maine coon","siames","ragdoll","sphynx"]
>>> for x in gatos:
	print(x)

	
persa
maine coon
siames
ragdoll
sphynx
>>> gatos
['persa', 'maine coon', 'siames', 'ragdoll', 'sphynx']
>>> gatos=["persa","maine coon","siames","ragdoll","sphynx"]
>>> gatos.append('birmanes')
>>> gatos
['persa', 'maine coon', 'siames', 'ragdoll', 'sphynx', 'birmanes']
>>> gatos.append('noruegues')
>>> gatos
['persa', 'maine coon', 'siames', 'ragdoll', 'sphynx', 'birmanes', 'noruegues']
>>> gatos.remove('persa')
>>> gatos
['maine coon', 'siames', 'ragdoll', 'sphynx', 'birmanes', 'noruegues']
>>> gatos.reverse()
>>> 
>>> gatos
['noruegues', 'birmanes', 'sphynx', 'ragdoll', 'siames', 'maine coon']
>>> gatos.
SyntaxError: invalid syntax
>>> lista.count("siames")
0
>>> lista.count("birmanes")
0
>>> lista.pop('siames')
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    lista.pop('siames')
TypeError: 'str' object cannot be interpreted as an integer
>>> lista.pop()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    lista.pop()
IndexError: pop from empty list
>>> siames in lista
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    siames in lista
NameError: name 'siames' is not defined
>>> "siames" in lista
False
>>> "siames" in gato
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    "siames" in gato
NameError: name 'gato' is not defined
>>> "birmanes" in lista
False
>>> "siames" not in lista
True
>>> "ragdoll" not in lista
True
>>> "vira lata" in lista
False
>>> "vira lata" not in lista
True
>>> if vira lata not in lista:
	
SyntaxError: invalid syntax
>>> if "vira lata" not in lista
SyntaxError: invalid syntax
>>> if 'exotico' not in lista
SyntaxError: invalid syntax
>>> 'exotico' not in lista
True
>>> if 'exotico' not in lista:
	print ('esta na lista')

	
esta na lista
>>> lista.index('siames')
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    lista.index('siames')
ValueError: 'siames' is not in list
>>> if 'exotico' not in lista:
	print ('esta na lista')

	
esta na lista
>>> lista.carro[2]
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    lista.carro[2]
AttributeError: 'list' object has no attribute 'carro'
>>> if 'exotico' not in lista:
	print ('esta na lista')

	
esta na lista
>>> lista.sort()
>>> lista.sort('gatos')
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    lista.sort('gatos')
TypeError: sort() takes no positional arguments
>>> lista.sort()
>>> 
>>> lista
[]
>>> gatos
['noruegues', 'birmanes', 'sphynx', 'ragdoll', 'siames', 'maine coon']
>>> gatos.sort()
>>> gatos
['birmanes', 'maine coon', 'noruegues', 'ragdoll', 'siames', 'sphynx']
>>> chr(65)
'A'
>>> chr(66)
'B'
>>> ascii("A")
"'A'"
>>> acii("a")
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    acii("a")
NameError: name 'acii' is not defined
>>> ascii("a")
"'a'"
>>> ord("A")
65
>>> chr(65)
'A'
>>> for num in range(65,91):
	print(chr(num),end=' ')

	
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
>>> for num in range(26,91):
	print(chr(num),end=' ')

	
        ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
>>> 
============= RESTART: D:/curso python ketlyn/Aula 3/verifica.py =============
digite uma cor preto
>>> 
============= RESTART: D:/curso python ketlyn/Aula 3/verifica.py =============
digite uma cor: preto
>>> 
>>> cor
'preto'
>>> 
============= RESTART: D:/curso python ketlyn/Aula 3/verifica.py =============
digite uma cor: preto
Traceback (most recent call last):
  File "D:/curso python ketlyn/Aula 3/verifica.py", line 11, in <module>
    if cor in cores:
NameError: name 'cores' is not defined
>>> 
============= RESTART: D:/curso python ketlyn/Aula 3/verifica.py =============
digite uma cor: preto
ta na lista
>>> 
============= RESTART: D:/curso python ketlyn/Aula 3/verifica.py =============
digite uma cor: preto
ta na lista
>>> 
============= RESTART: D:/curso python ketlyn/Aula 3/verifica.py =============
digite uma cor: roxo
nao ta
>>> 
============= RESTART: D:/curso python ketlyn/Aula 3/verifica.py =============
digite uma cor: preto
ta na lista
>>> cores
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    cores
NameError: name 'cores' is not defined
>>> cor
'preto'
>>> lista.cor
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    lista.cor
AttributeError: 'list' object has no attribute 'cor'
>>> lista
['azul', 'amarelo', 'preto', 'azul', 'branco', 'rosa', 'preto', 'laranja']
>>> 
============= RESTART: D:/curso python ketlyn/Aula 3/verifica.py =============
digite uma cor: roxo
nao ta
>>> lista
['azul', 'amarelo', 'preto', 'azul', 'branco', 'rosa', 'preto', 'laranja', 'roxo']
>>> 
============= RESTART: D:/curso python ketlyn/Aula 3/verifica.py =============
digite uma cor: verde
nao ta
>>> lista
['azul', 'amarelo', 'preto', 'azul', 'branco', 'rosa', 'preto', 'laranja', 'verde']
>>> 
============= RESTART: D:/curso python ketlyn/Aula 3/verifica.py =============
digite uma cor: pastel
nao ta
>>> lista
['azul', 'amarelo', 'preto', 'azul', 'branco', 'rosa', 'preto', 'laranja', 'pastel']
>>> 
============== RESTART: D:/curso python ketlyn/Aula 3/login.py ==============
digite seu usuario bruna
>>> 
>>> 
============== RESTART: D:/curso python ketlyn/Aula 3/login.py ==============
digite seu usuario
============== RESTART: D:/curso python ketlyn/Aula 3/login.py ==============
digite seu usuario: bruna
invalido
>>> 
============== RESTART: D:/curso python ketlyn/Aula 3/login.py ==============
>>> 
digite seu usuario: Bruna
valido
>>> 'jose da silva'.capitalize ()
'Jose da silva'
>>> 'jose da silva'.endswith('silva')
True
>>> 'jose da silva'.startswith('jose')
True
>>> 'JOSE DA SILVA'.lower()
'jose da silva'
>>> 'jose da silva'.upper()
'JOSE DA SILVA'
>>> 'jose da silva'.title()
'Jose Da Silva'
>>> 'jose da silva'.split()
['jose', 'da', 'silva']
>>> nome='jose da silva'
>>> lista=nome.split()
>>> lista
['jose', 'da', 'silva']
>>> lista[0]
'jose'
>>> lista[1]
'da'
>>> lista[2]
'silva'
>>> 'jose da silva'.split()[2]
'silva'
>>> '  jose  da  silva  '.strip()
'jose  da  silva'
>>> 'jose da silva'.count("a")
2
>>> 
============== RESTART: D:/curso python ketlyn/Aula 3/login.py ==============
digite seu usuario: Bruna
valido
>>> 
============== RESTART: D:/curso python ketlyn/Aula 3/login.py ==============
digite seu usuario: 
invalido
>>> 
============== RESTART: D:/curso python ketlyn/Aula 3/login.py ==============
digite seu usuario: BRUNA
valido
>>> 
============== RESTART: D:/curso python ketlyn/Aula 3/login.py ==============
digite seu usuario: CARLOS
invalido
>>> 
