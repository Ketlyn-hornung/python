Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> lista=[1,2,3,4,5,6,7,8,9]
>>> lista[0]
1
>>> lista[0:5]
[1, 2, 3, 4, 5]
>>> lista=[0,1,2,3,4,5,6,7,7,9,10,11,12]
>>> lista[0]
0
>>> lista[12]
12
>>> lista[7:11]
[7, 7, 9, 10]
>>> lista[0:11]
[0, 1, 2, 3, 4, 5, 6, 7, 7, 9, 10]
>>> lista[:11]
[0, 1, 2, 3, 4, 5, 6, 7, 7, 9, 10]
>>> lista[7:]
[7, 7, 9, 10, 11, 12]
>>> lista[0:12]
[0, 1, 2, 3, 4, 5, 6, 7, 7, 9, 10, 11]
>>> lista[0:13]
[0, 1, 2, 3, 4, 5, 6, 7, 7, 9, 10, 11, 12]
>>> lista[0:13:2]
[0, 2, 4, 6, 7, 10, 12]
>>> lista[0:13:5]
[0, 5, 10]
>>> lista[::2]
[0, 2, 4, 6, 7, 10, 12]
>>> lista=[1,2,3[4,5,6[7,8,9]]]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    lista=[1,2,3[4,5,6[7,8,9]]]
TypeError: 'int' object is not subscriptable
>>> lista=[1,2,3,[4,5,6,[7,8,9]]]
>>> lista[0]
1
>>> lista[1]
2
>>> lista[2]
3
>>> lista[3]
[4, 5, 6, [7, 8, 9]]
>>> lista[3][0]
4
>>> lista[3][1]
5
>>> lista[3][2]
6
>>> lista[3][3]
[7, 8, 9]
>>> lista[3][3][0]
7
>>> lista[3][3][1]
8
>>> lista[3][3][2]
9
>>> lista=[0,1,2,3,4,5]
>>> lista[-1]
5
>>> lista[-2]
4
>>> lista[-3]
3
>>> lista[-2:]
[4, 5]
>>> lista[-3:]
[3, 4, 5]
>>> lista[-3:-6]
[]
>>> lista[-3:-1]
[3, 4]
>>> 
================= RESTART: D:/curso python ketlyn/aula 5.py =================
8
>>> 
================= RESTART: D:/curso python ketlyn/aula 5.py =================
matriz usando lista...
[3, 2, 6]
[3, 3, 8]
[1, 2, 3]
numero da linha:2
numero da coluna:1
2
>>> 3
3
>>> 
>>> 
================= RESTART: D:/curso python ketlyn/aula 5.py =================
matriz usando lista...
[3, 2, 6]
[3, 3, 8]
[1, 2, 3]
numero da linha:
Traceback (most recent call last):
  File "D:/curso python ketlyn/aula 5.py", line 15, in <module>
    lin = int(input('numero da linha:'))
ValueError: invalid literal for int() with base 10: ''
>>> 
================= RESTART: D:/curso python ketlyn/aula 5.py =================
matriz usando lista...
[3, 2, 6]
[3, 3, 8]
[1, 2, 3]
numero da linha:3
numero da coluna:3
Traceback (most recent call last):
  File "D:/curso python ketlyn/aula 5.py", line 18, in <module>
    print(matriz[lin][col])
IndexError: list index out of range
>>> 3
3
>>> 
================= RESTART: D:/curso python ketlyn/aula 5.py =================
matriz usando lista...
[3, 2, 6]
[3, 3, 8]
[1, 2, 3]
numero da linha:
Traceback (most recent call last):
  File "D:/curso python ketlyn/aula 5.py", line 15, in <module>
    lin = int(input('numero da linha:'))
ValueError: invalid literal for int() with base 10: ''
>>> 
================= RESTART: D:/curso python ketlyn/aula 5.py =================
matriz usando lista...
[3, 2, 6]
[3, 3, 8]
[1, 2, 3]
numero da linha:3
numero da coluna:2
Traceback (most recent call last):
  File "D:/curso python ketlyn/aula 5.py", line 18, in <module>
    print(matriz[lin][col])
IndexError: list index out of range
>>> 
================= RESTART: D:/curso python ketlyn/aula 5.py =================
matriz usando lista...
[3, 2, 6]
[3, 3, 8]
[1, 2, 3]
numero da linha:2
numero da coluna:3
Traceback (most recent call last):
  File "D:/curso python ketlyn/aula 5.py", line 18, in <module>
    print(matriz[lin][col])
IndexError: list index out of range
>>> 
================= RESTART: D:/curso python ketlyn/aula 5.py =================
matriz usando lista...
[3, 2, 6]
[3, 3, 8]
[1, 2, 3]
numero da linha:2
numero da coluna:2
3
>>> 
================= RESTART: D:/curso python ketlyn/aula 5.py =================
matriz usando lista...
[3, 2, 6]
[3, 3, 8]
[1, 2, 3]
numero da linha:2
numero da coluna:1
2
>>> 
=========== RESTART: D:/curso python ketlyn/aula 5/matriz numpy.py ===========
matriz usando numpy
[[1 2 5]
 [3 7 5]
 [9 0 4]]
>>> 
=========== RESTART: D:/curso python ketlyn/aula 5/matriz numpy.py ===========
matriz usando numpy
[[1 2 5]
 [3 7 5]
 [9 0 4]]
>>> 0*5
0
>>> 1*5
5
>>> [0]*5
[0, 0, 0, 0, 0]
>>> [1]*10
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
>>> 
================= RESTART: D:/curso python ketlyn/aula 5.py =================
matriz usando lista...
[3, 2, 6]
[3, 3, 8]
[1, 2, 3]
numero da linha:2
numero da coluna:2
3
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
>>> 
================= RESTART: D:/curso python ketlyn/aula 5.py =================
matriz usando lista...
[3, 2, 6]
[3, 3, 8]
[1, 2, 3]
numero da linha:1
numero da coluna:1
3
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
>>> [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
>>> 
>>> import random
>>> random.randrange(10)
6
>>> random.randrange(10)
4
>>> random
<module 'random' from 'C:\\Users\\LAB 03\\AppData\\Local\\Programs\\Python\\Python37-32\\lib\\random.py'>
>>> random.randrange(10)
7
>>> random.randrange(10)
2
>>> random.randrange(10)
1
>>> random.randrange(10)
3
>>> randrange
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    randrange
NameError: name 'randrange' is not defined
>>> random.randrange(10)
3
>>> random.randrange(10)
2
>>> random.randrange(10)
2
>>> random.randrange(1,101)
89
>>> random.randrange(1,101)
79
>>> random.randrange(1,101)
76
>>> random.randrange(1,101)
26
>>> random.randrange(1,101)
58
>>> random.randrange(1,101)
9
>>> random.randrange(1,101)
31
>>> 
============ RESTART: D:/curso python ketlyn/aula 5/advinhaçao.py ============
>>> 
============ RESTART: D:/curso python ketlyn/aula 5/advinhaçao.py ============
**************************88***
bem vindo ao jogo de advinhaçao
*******************************
>>> 
============ RESTART: D:/curso python ketlyn/aula 5/advinhaçao.py ============
*******************************
bem vindo ao jogo de advinhaçao
*******************************
>>> 
============ RESTART: D:/curso python ketlyn/aula 5/advinhaçao.py ============
*******************************
bem vindo ao jogo de advinhaçao
*******************************
digite um numero entre 1 e 100:2
>>> 
============ RESTART: D:/curso python ketlyn/aula 5/advinhaçao.py ============
*******************************
bem vindo ao jogo de advinhaçao
*******************************
digite um numero entre 1 e 100:3
errou
>>> 
============ RESTART: D:/curso python ketlyn/aula 5/advinhaçao.py ============
*******************************
bem vindo ao jogo de advinhaçao
*******************************
97
digite um numero entre 1 e 100:39
errou
>>> 
============ RESTART: D:/curso python ketlyn/aula 5/advinhaçao.py ============
*******************************
bem vindo ao jogo de advinhaçao

*******************************
95
digite um numero entre 1 e 100:97
errou
>>> 
============ RESTART: D:/curso python ketlyn/aula 5/advinhaçao.py ============
*******************************
bem vindo ao jogo de advinhaçao
*******************************
50
digite um numero entre 1 e 100:
Traceback (most recent call last):
  File "D:/curso python ketlyn/aula 5/advinhaçao.py", line 12, in <module>
    chute=int(input('digite um numero entre 1 e 100:'))
ValueError: invalid literal for int() with base 10: ''
>>> 
============ RESTART: D:/curso python ketlyn/aula 5/advinhaçao.py ============
*******************************
bem vindo ao jogo de advinhaçao
*******************************
88
digite um numero entre 1 e 100:88
acertou
>>> 
============ RESTART: D:/curso python ketlyn/aula 5/advinhaçao.py ============
*******************************
bem vindo ao jogo de advinhaçao
*******************************
digite um numero entre 1 e 100:3
errou
digite um numero entre 1 e 100:5
errou
digite um numero entre 1 e 100:26
errou
digite um numero entre 1 e 100:39
errou
digite um numero entre 1 e 100:55
errou
digite um numero entre 1 e 100:40
errou
digite um numero entre 1 e 100:2
errou
digite um numero entre 1 e 100:2
errou
digite um numero entre 1 e 100:2
errou
digite um numero entre 1 e 100:74
errou
digite um numero entre 1 e 100:73
errou
digite um numero entre 1 e 100:22
errou
digite um numero entre 1 e 100:45
errou
digite um numero entre 1 e 100:85
errou
digite um numero entre 1 e 100:94
errou
digite um numero entre 1 e 100:52
errou
digite um numero entre 1 e 100:14
errou
digite um numero entre 1 e 100:73
errou
digite um numero entre 1 e 100:15
errou
digite um numero entre 1 e 100:47
errou
>>> 75
75
>>> 47
47
>>> 
============ RESTART: D:/curso python ketlyn/aula 5/advinhaçao.py ============
*******************************
bem vindo ao jogo de advinhaçao
*******************************
tentativa1de20
digite um numero entre 1 e 100:2
errou
tentativa2de20
digite um numero entre 1 e 100:
============ RESTART: D:/curso python ketlyn/aula 5/advinhaçao.py ============
*******************************
bem vindo ao jogo de advinhaçao
*******************************
61
tentativa1de 20
digite um numero entre 1 e 100:5
Errou! seu chute foi menor que o numero secreto
tentativa2de 20
digite um numero entre 1 e 100:3
Errou! seu chute foi menor que o numero secreto
tentativa3de 20
digite um numero entre 1 e 100:4
Errou! seu chute foi menor que o numero secreto
tentativa4de 20
digite um numero entre 1 e 100:62
Errou! seu chute foi maior que o numero secreto
tentativa5de 20
digite um numero entre 1 e 100:99
Errou! seu chute foi maior que o numero secreto
tentativa6de 20
digite um numero entre 1 e 100:52
Errou! seu chute foi menor que o numero secreto
tentativa7de 20
digite um numero entre 1 e 100:45
Errou! seu chute foi menor que o numero secreto
tentativa8de 20
digite um numero entre 1 e 100:28
Errou! seu chute foi menor que o numero secreto
tentativa9de 20
digite um numero entre 1 e 100:16
Errou! seu chute foi menor que o numero secreto
tentativa10de 20
digite um numero entre 1 e 100:15
Errou! seu chute foi menor que o numero secreto
tentativa11de 20
digite um numero entre 1 e 100:13
Errou! seu chute foi menor que o numero secreto
tentativa12de 20
digite um numero entre 1 e 100:4
Errou! seu chute foi menor que o numero secreto
tentativa13de 20
digite um numero entre 1 e 100:7
Errou! seu chute foi menor que o numero secreto
tentativa14de 20
digite um numero entre 1 e 100:8
Errou! seu chute foi menor que o numero secreto
tentativa15de 20
digite um numero entre 1 e 100:10
Errou! seu chute foi menor que o numero secreto
tentativa16de 20
digite um numero entre 1 e 100:24
Errou! seu chute foi menor que o numero secreto
tentativa17de 20
digite um numero entre 1 e 100:27
Errou! seu chute foi menor que o numero secreto
tentativa18de 20
digite um numero entre 1 e 100:29
Errou! seu chute foi menor que o numero secreto
tentativa19de 20
digite um numero entre 1 e 100:30
Errou! seu chute foi menor que o numero secreto
tentativa20de 20
digite um numero entre 1 e 100:31
Errou! seu chute foi menor que o numero secreto
>>> 
============ RESTART: D:/curso python ketlyn/aula 5/advinhaçao.py ============
*******************************
bem vindo ao jogo de advinhaçao
*******************************
1
tentativa1de 20
digite um numero entre 1 e 100:2
Errou! seu chute foi maior que o numero secreto
tentativa2de 20
digite um numero entre 1 e 100:3
Errou! seu chute foi maior que o numero secreto
tentativa3de 20
digite um numero entre 1 e 100:4
Errou! seu chute foi maior que o numero secreto
tentativa4de 20
digite um numero entre 1 e 100:5
Errou! seu chute foi maior que o numero secreto
tentativa5de 20
digite um numero entre 1 e 100:6
Errou! seu chute foi maior que o numero secreto
tentativa6de 20
digite um numero entre 1 e 100:7
Errou! seu chute foi maior que o numero secreto
tentativa7de 20
digite um numero entre 1 e 100:8
Errou! seu chute foi maior que o numero secreto
tentativa8de 20
digite um numero entre 1 e 100:9
Errou! seu chute foi maior que o numero secreto
tentativa9de 20
digite um numero entre 1 e 100:10
Errou! seu chute foi maior que o numero secreto
tentativa10de 20
digite um numero entre 1 e 100:11
Errou! seu chute foi maior que o numero secreto
tentativa11de 20
digite um numero entre 1 e 100:12
Errou! seu chute foi maior que o numero secreto
tentativa12de 20
digite um numero entre 1 e 100:13
Errou! seu chute foi maior que o numero secreto
tentativa13de 20
digite um numero entre 1 e 100:14
Errou! seu chute foi maior que o numero secreto
tentativa14de 20
digite um numero entre 1 e 100:15
Errou! seu chute foi maior que o numero secreto
tentativa15de 20
digite um numero entre 1 e 100:16
Errou! seu chute foi maior que o numero secreto
tentativa16de 20
digite um numero entre 1 e 100:17
Errou! seu chute foi maior que o numero secreto
tentativa17de 20
digite um numero entre 1 e 100:18
Errou! seu chute foi maior que o numero secreto
tentativa18de 20
digite um numero entre 1 e 100:19
Errou! seu chute foi maior que o numero secreto
tentativa19de 20
digite um numero entre 1 e 100:20
Errou! seu chute foi maior que o numero secreto
tentativa20de 20
digite um numero entre 1 e 100:
Traceback (most recent call last):
  File "D:/curso python ketlyn/aula 5/advinhaçao.py", line 16, in <module>
    chute=int(input('digite um numero entre 1 e 100:'))
ValueError: invalid literal for int() with base 10: ''
>>> 
============ RESTART: D:/curso python ketlyn/aula 5/advinhaçao.py ============
*******************************
bem vindo ao jogo de advinhaçao
*******************************
Qual o nivel de dificulade?
(1) Facil (2)Medio (3) Dificil
defina o nivel:2
tentativa1de 10
digite um numero entre 1 e 100:5
Errou! seu chute foi menor que o numero secreto
tentativa2de 10
digite um numero entre 1 e 100:6
Errou! seu chute foi menor que o numero secreto
tentativa3de 10
digite um numero entre 1 e 100:4
Errou! seu chute foi menor que o numero secreto
tentativa4de 10
digite um numero entre 1 e 100:5
Errou! seu chute foi menor que o numero secreto
tentativa5de 10
digite um numero entre 1 e 100:10
Errou! seu chute foi menor que o numero secreto
tentativa6de 10
digite um numero entre 1 e 100:11
Errou! seu chute foi menor que o numero secreto
tentativa7de 10
digite um numero entre 1 e 100:12
Errou! seu chute foi menor que o numero secreto
tentativa8de 10
digite um numero entre 1 e 100:13
Errou! seu chute foi menor que o numero secreto
tentativa9de 10
digite um numero entre 1 e 100:14
Errou! seu chute foi menor que o numero secreto
tentativa10de 10
digite um numero entre 1 e 100:15
Errou! seu chute foi menor que o numero secreto
***Fim de jogo***
 O numero secreto era 49
>>> 
============ RESTART: D:/curso python ketlyn/aula 5/advinhaçao.py ============
*******************************
bem vindo ao jogo de advinhaçao
*******************************
Qual o nivel de dificulade?
(1) Facil (2)Medio (3) Dificil
defina o nivel:3
tentativa1de 5
digite um numero entre 1 e 100:5
Errou! seu chute foi menor que o numero secreto
tentativa2de 5
digite um numero entre 1 e 100:10
Errou! seu chute foi menor que o numero secreto
tentativa3de 5
digite um numero entre 1 e 100:29
Errou! seu chute foi menor que o numero secreto
tentativa4de 5
digite um numero entre 1 e 100:30
Errou! seu chute foi menor que o numero secreto
tentativa5de 5
digite um numero entre 1 e 100:40
Errou! seu chute foi menor que o numero secreto
***Fim de jogo***
 O numero secreto era 87
>>> 
============ RESTART: D:/curso python ketlyn/aula 5/advinhaçao.py ============
*******************************
bem vindo ao jogo de advinhaçao
*******************************
Qual o nivel de dificulade?
(1) Facil (2)Medio (3) Dificil
defina o nivel:1
tentativa1de 20
digite um numero entre 1 e 100:
============ RESTART: D:/curso python ketlyn/aula 5/advinhaçao.py ============
*******************************
bem vindo ao jogo de advinhaçao
*******************************
Qual o nivel de dificulade?
(1) Facil (2)Medio (3) Dificil
defina o nivel:3
tentativa1de 5
digite um numero entre 1 e 100:55
Errou! seu chute foi maior que o numero secreto
tentativa2de 5
digite um numero entre 1 e 100:77
Errou! seu chute foi maior que o numero secreto
tentativa3de 5
digite um numero entre 1 e 100:12
Errou! seu chute foi menor que o numero secreto
tentativa4de 5
digite um numero entre 1 e 100:44
Errou! seu chute foi menor que o numero secreto
tentativa5de 5
digite um numero entre 1 e 100:45
Errou! seu chute foi menor que o numero secreto
***Fim de jogo***
 O numero secreto era 49. Voce fez 1000pontos.
>>> 
============ RESTART: D:/curso python ketlyn/aula 5/advinhaçao.py ============
>>> 
============ RESTART: D:/curso python ketlyn/aula 5/advinhaçao.py ============
*******************************
bem vindo ao jogo de advinhaçao
*******************************
Qual o nivel de dificulade?
(1) Facil (2)Medio (3) Dificil
defina o nivel:3
tentativa1de 5
digite um numero entre 1 e 100:5
Errou! seu chute foi menor que o numero secreto
tentativa2de 5
digite um numero entre 1 e 100:10
Errou! seu chute foi menor que o numero secreto
tentativa3de 5
digite um numero entre 1 e 100:36
Errou! seu chute foi menor que o numero secreto
tentativa4de 5
digite um numero entre 1 e 100:42
Errou! seu chute foi menor que o numero secreto
tentativa5de 5
digite um numero entre 1 e 100:55
Errou! seu chute foi menor que o numero secreto
***Fim de jogo***
 O numero secreto era 73. Voce fez 1000pontos.
>>> 455
455
>>> 
============ RESTART: D:/curso python ketlyn/aula 5/advinhaçao.py ============
***Fim de jogo***
Traceback (most recent call last):
  File "D:/curso python ketlyn/aula 5/advinhaçao.py", line 44, in <module>
    print(f' O numero secreto era {numero_secreto}. Voce fez {pontos}pontos.')
NameError: name 'numero_secreto' is not defined
>>> 
============ RESTART: D:/curso python ketlyn/aula 5/parametros.py ============
bom dia
>>> 
============ RESTART: D:/curso python ketlyn/aula 5/parametros.py ============
Bom dia
Boa tarde
Boa noite
>>> 
============ RESTART: D:/curso python ketlyn/aula 5/parametros.py ============
Bom dia
Boa tarde
Boa noite
>>> 
============ RESTART: D:/curso python ketlyn/aula 5/parametros.py ============
Bom dia
Boa tarde
Boa noite
>>> 
============ RESTART: D:/curso python ketlyn/aula 5/parametros.py ============
Bom dia
Boa tarde
Boa noite
>>> 
============ RESTART: D:/curso python ketlyn/aula 5/parametros.py ============
Mensagem:Bom dia
Mensagem:Boa tarde
Mensagem:Boa noite
>>> 
============ RESTART: D:/curso python ketlyn/aula 5/parametros.py ============
Alerta:Bom dia
Boa tarde:Bom dia
Traceback (most recent call last):
  File "D:/curso python ketlyn/aula 5/parametros.py", line 10, in <module>
    mensagem('Boa noite',tipo='Alerta')
TypeError: mensagem() got multiple values for argument 'tipo'
>>> 
============ RESTART: D:/curso python ketlyn/aula 5/parametros.py ============
Alerta:Bom dia
Boa tarde:Bom dia
Traceback (most recent call last):
  File "D:/curso python ketlyn/aula 5/parametros.py", line 10, in <module>
    mensagem('Boa noite',tipo='Alerta')
TypeError: mensagem() got multiple values for argument 'tipo'
>>> 
============ RESTART: D:/curso python ketlyn/aula 5/parametros.py ============
Alerta:Bom dia
Mensagem:Boa tarde
Alerta:Boa noite
123
>>> 
========== RESTART: D:/curso python ketlyn/aula 5/arquivo texto.py ==========
>>> 
========== RESTART: D:/curso python ketlyn/aula 5/arquivo texto.py ==========
>>> 
========== RESTART: D:/curso python ketlyn/aula 5/arquivo texto.py ==========
>>> 
========== RESTART: D:/curso python ketlyn/aula 5/arquivo texto.py ==========
>>> 
========== RESTART: D:/curso python ketlyn/aula 5/arquivo texto.py ==========
>>> 
========== RESTART: D:/curso python ketlyn/aula 5/arquivo texto.py ==========
quantas frutas voce quer digitar?3
Digita a fruta 1:uva
Digita a fruta 2:morango
Digita a fruta 3:banana
['uva', 'morango', 'banana']
>>> 
