Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
========== RESTART: D:/curso python ketlyn/Aula 4/aula 4 estoque.py ==========
digite o nome do produto:geladeira
digite a quantidade:10
>>> produto
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    produto
NameError: name 'produto' is not defined
>>> produtos
[]
>>> 
========== RESTART: D:/curso python ketlyn/Aula 4/aula 4 estoque.py ==========
digite o nome do produto:geladeira
digite a quantidade:10
['geladeira']
Traceback (most recent call last):
  File "D:/curso python ketlyn/Aula 4/aula 4 estoque.py", line 23, in <module>
    print(quantidades)
NameError: name 'quantidades' is not defined
>>> 
========== RESTART: D:/curso python ketlyn/Aula 4/aula 4 estoque.py ==========
digite o nome do produto:geladeira
digite a quantidades:10
['geladeira']
[10]
>>> 
========== RESTART: D:/curso python ketlyn/Aula 4/aula 4 estoque.py ==========
digite o nome do produto:tv
digite a quantidades:8
['tv']
[8]
>>> produtos
['tv']
>>> quant
8
>>> 
========== RESTART: D:/curso python ketlyn/Aula 4/aula 4 estoque.py ==========
digite o nome do produto:fogao
digite a quantidades:7
['fogao']
[7]
digite o nome do produto:tv
digite a quantidades:15
['fogao', 'tv']
[7, 15]
digite o nome do produto:
========== RESTART: D:/curso python ketlyn/Aula 4/aula 4 estoque.py ==========
digite o nome do produto:fogao
digite a quantidades:5
['fogao']
[5]
Quer continuar?(S)im ou (N)ao:s
digite o nome do produto:fogao
digite a quantidades:10
['fogao', 'fogao']
[5, 10]
Quer continuar?(S)im ou (N)ao:n
digite o nome do produto:N
digite a quantidades:5
['fogao', 'fogao', 'N']
[5, 10, 5]
Quer continuar?(S)im ou (N)ao:N
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
========== RESTART: D:/curso python ketlyn/Aula 4/aula 4 estoque.py ==========
digite o nome do produto:geladeira
digite a quantidades:10
['geladeira']
[10]
Quer continuar?(S)im ou (N)ao:n
>>> 
========== RESTART: D:/curso python ketlyn/Aula 4/aula 4 estoque.py ==========
>>> 
digite o nome do produto:fogao
digite a quantidades:5
['fogao']
[5]
Quer continuar?(S)im ou (N)ao:s
digite o nome do produto:tv
digite a quantidades:5
['fogao', 'tv']
[5, 5]
Quer continuar?(S)im ou (N)ao:n
>>> 
========== RESTART: D:/curso python ketlyn/Aula 4/aula 4 estoque.py ==========
Traceback (most recent call last):
  File "D:/curso python ketlyn/Aula 4/aula 4 estoque.py", line 8, in <module>
    while resp == 'S':
NameError: name 'resp' is not defined
>>> 
========== RESTART: D:/curso python ketlyn/Aula 4/aula 4 estoque.py ==========
Quer continuar?(S)im ou (N)ao:s
digite o nome do produto:geladeira
digite a quantidades:5
['geladeira']
[5]
digite o nome do produto:
========== RESTART: D:/curso python ketlyn/Aula 4/aula 4 estoque.py ==========
digite o nome do produto:fogao
digite a quantidades:5
['fogao']
[5]
Quer continuar?(S)im ou (N)ao:s
digite o nome do produto:tv
digite a quantidades:8
['fogao', 'tv']
[5, 8]
Quer continuar?(S)im ou (N)ao:n
>>> 
========== RESTART: D:/curso python ketlyn/Aula 4/aula 4 estoque.py ==========
######## Magazine da Maria ########
 Sistema de Controle de Estoque-Versao 1.0#
#   Desenvolvido por: Ketlyn              #
1= Cadastrar
2= Listar
3= Sair
digite o nome do produto:fogao
digite a quantidades:5
['fogao']
[5]
Quer continuar?(S)im ou (N)ao:s
digite o nome do produto:geladeira
digite a quantidades:10
['fogao', 'geladeira']
[5, 10]
Quer continuar?(S)im ou (N)ao:s
digite o nome do produto:tv 
digite a quantidades:15
['fogao', 'geladeira', 'tv ']
[5, 10, 15]
Quer continuar?(S)im ou (N)ao:n
>>> 
========== RESTART: D:/curso python ketlyn/Aula 4/aula 4 estoque.py ==========
digite o nome do produto:geladeira
digite a quantidades:10
['geladeira']
[10]
Quer continuar?(S)im ou (N)ao:s
digite o nome do produto:5
digite a quantidades:10
['geladeira', '5']
[10, 10]
Quer continuar?(S)im ou (N)ao:n
>>> 
========== RESTART: D:/curso python ketlyn/Aula 4/aula 4 estoque.py ==========
>>> 
========== RESTART: D:/curso python ketlyn/Aula 4/aula 4 estoque.py ==========
######## Magazine da Maria ########
 Sistema de Controle de Estoque-Versao 1.0#
#   Desenvolvido por: Ketlyn              #
1= Cadastrar
2= Listar
3= Sair
>>> 1
1
>>> 
========== RESTART: D:/curso python ketlyn/Aula 4/aula 4 estoque.py ==========
######## Magazine da Maria ########
 Sistema de Controle de Estoque-Versao 1.0#
#   Desenvolvido por: Ketlyn              #
1= Cadastrar
2= Listar
3= Sair
qual opçao?1
Traceback (most recent call last):
  File "D:/curso python ketlyn/Aula 4/aula 4 estoque.py", line 50, in <module>
    menu()
  File "D:/curso python ketlyn/Aula 4/aula 4 estoque.py", line 20, in menu
    cadstrar()
NameError: name 'cadstrar' is not defined
>>> 
========== RESTART: D:/curso python ketlyn/Aula 4/aula 4 estoque.py ==========
######## Magazine da Maria ########
 Sistema de Controle de Estoque-Versao 1.0#
#   Desenvolvido por: Ketlyn              #
1= Cadastrar
2= Listar
3= Sair
qual opçao?1
digite o nome do produto:geladeira
digite a quantidades:5
['geladeira']
[5]
Quer continuar?(S)im ou (N)ao:s
digite o nome do produto:fogao
digite a quantidades:10
['geladeira', 'fogao']
[5, 10]
Quer continuar?(S)im ou (N)ao:n
>>> 
========== RESTART: D:/curso python ketlyn/Aula 4/aula 4 estoque.py ==========
######## Magazine da Maria ########
 Sistema de Controle de Estoque-Versao 1.0#
#   Desenvolvido por: Ketlyn              #
1= Cadastrar
2= Listar
3= Sair
qual opçao?3
>>> 
========== RESTART: D:/curso python ketlyn/Aula 4/aula 4 estoque.py ==========
######## Magazine da Maria ########
 Sistema de Controle de Estoque-Versao 1.0#
#   Desenvolvido por: Ketlyn              #
1= Cadastrar
2= Listar
3= Sair
qual opçao?4
>>> 
========== RESTART: D:/curso python ketlyn/Aula 4/aula 4 estoque.py ==========
######## Magazine da Maria ########
 Sistema de Controle de Estoque-Versao 1.0#
#   Desenvolvido por: Ketlyn              #
1= Cadastrar
2= Listar
3= Sair
qual opçao?2
[]
[]
>>> 
========== RESTART: D:/curso python ketlyn/Aula 4/aula 4 estoque.py ==========
######## Magazine da Maria ########
 Sistema de Controle de Estoque-Versao 1.0#
#   Desenvolvido por: Ketlyn              #
1= Cadastrar
2= Listar
3= Sair
qual opçao?1
digite o nome do produto:fogao
digite a quantidades:10
Quer continuar?(S)im ou (N)ao:geladeira
>>> 10
10
>>> 2
2
>>> 
========== RESTART: D:/curso python ketlyn/Aula 4/aula 4 estoque.py ==========
######## Magazine da Maria ########
 Sistema de Controle de Estoque-Versao 1.0#
#   Desenvolvido por: Ketlyn              #
1= Cadastrar
2= Listar
3= Sair
qual opçao?3
Saindo...Adeus!
>>> 
========== RESTART: D:/curso python ketlyn/Aula 4/aula 4 estoque.py ==========
######## Magazine da Maria ########
 Sistema de Controle de Estoque-Versao 1.0#
#   Desenvolvido por: Ketlyn              #
1= Cadastrar
2= Listar
3= Sair
qual opçao?6
opçao invalida
>>> 
========== RESTART: D:/curso python ketlyn/Aula 4/aula 4 estoque.py ==========
######## Magazine da Maria ########
 Sistema de Controle de Estoque-Versao 1.0#
#   Desenvolvido por: Ketlyn              #
1= Cadastrar
2= Listar
3= Sair
qual opçao?0
opçao invalida
>>> 
========== RESTART: D:/curso python ketlyn/Aula 4/aula 4 estoque.py ==========
######## Magazine da Maria ########
 Sistema de Controle de Estoque-Versao 1.0#
#   Desenvolvido por: Ketlyn              #
1= Cadastrar
2= Listar
3= Sair
qual opçao?4
opçao invalida
>>> 
========== RESTART: D:/curso python ketlyn/Aula 4/aula 4 estoque.py ==========
######## Magazine da Maria ########
 Sistema de Controle de Estoque-Versao 1.0#
#   Desenvolvido por: Ketlyn              #
1= Cadastrar
2= Listar
3= Sair
qual opçao?2
[]
[]
>>> 
========== RESTART: D:/curso python ketlyn/Aula 4/aula 4 estoque.py ==========
######## Magazine da Maria ########
 Sistema de Controle de Estoque-Versao 1.0#
#   Desenvolvido por: Ketlyn              #
1= Cadastrar
2= Listar
3= Sair
qual opçao?1
digite o nome do produto:cadastrar
digite a quantidades:5
Quer continuar?(S)im ou (N)ao:n
>>> 
========== RESTART: D:/curso python ketlyn/Aula 4/aula 4 estoque.py ==========
Traceback (most recent call last):
  File "D:/curso python ketlyn/Aula 4/aula 4 estoque.py", line 61, in <module>
    menu()
  File "D:/curso python ketlyn/Aula 4/aula 4 estoque.py", line 9, in menu
    while opcao !=3:
UnboundLocalError: local variable 'opcao' referenced before assignment
>>> 
========== RESTART: D:/curso python ketlyn/Aula 4/aula 4 estoque.py ==========
######## Magazine da Maria ########
 Sistema de Controle de Estoque-Versao 1.0#
#   Desenvolvido por: Ketlyn              #
1= Cadastrar
2= Listar
3= Sair
qual opçao?1
digite o nome do produto:tv
digite a quantidades:10
Quer continuar?(S)im ou (N)ao:s
digite o nome do produto:fogao
digite a quantidades:5
Quer continuar?(S)im ou (N)ao:n
######## Magazine da Maria ########
 Sistema de Controle de Estoque-Versao 1.0#
#   Desenvolvido por: Ketlyn              #
1= Cadastrar
2= Listar
3= Sair
qual opçao?2
['tv', 'fogao']
[10, 5]
######## Magazine da Maria ########
 Sistema de Controle de Estoque-Versao 1.0#
#   Desenvolvido por: Ketlyn              #
1= Cadastrar
2= Listar
3= Sair
qual opçao?2
['tv', 'fogao']
[10, 5]
######## Magazine da Maria ########
 Sistema de Controle de Estoque-Versao 1.0#
#   Desenvolvido por: Ketlyn              #
1= Cadastrar
2= Listar
3= Sair
qual opçao?2
['tv', 'fogao']
[10, 5]
######## Magazine da Maria ########
 Sistema de Controle de Estoque-Versao 1.0#
#   Desenvolvido por: Ketlyn              #
1= Cadastrar
2= Listar
3= Sair
qual opçao?2
['tv', 'fogao']
[10, 5]
######## Magazine da Maria ########
 Sistema de Controle de Estoque-Versao 1.0#
#   Desenvolvido por: Ketlyn              #
1= Cadastrar
2= Listar
3= Sair
qual opçao?
Traceback (most recent call last):
  File "D:/curso python ketlyn/Aula 4/aula 4 estoque.py", line 62, in <module>
    menu()
  File "D:/curso python ketlyn/Aula 4/aula 4 estoque.py", line 19, in menu
    opcao=int(input('qual opçao?'))
ValueError: invalid literal for int() with base 10: ''
>>> 
>>> 
>>> 
>>> 
========== RESTART: D:/curso python ketlyn/Aula 4/aula 4 estoque.py ==========
######## Magazine da Maria ########
 Sistema de Controle de Estoque-Versao 1.0#
#   Desenvolvido por: Ketlyn              #
1= Cadastrar
2= Listar
0= Sair
qual opçao?0
Saindo...Adeus!
######## Magazine da Maria ########
 Sistema de Controle de Estoque-Versao 1.0#
#   Desenvolvido por: Ketlyn              #
1= Cadastrar
2= Listar
0= Sair
qual opçao?0
Saindo...Adeus!
######## Magazine da Maria ########
 Sistema de Controle de Estoque-Versao 1.0#
#   Desenvolvido por: Ketlyn              #
1= Cadastrar
2= Listar
0= Sair
qual opçao?0
Saindo...Adeus!
######## Magazine da Maria ########
 Sistema de Controle de Estoque-Versao 1.0#
#   Desenvolvido por: Ketlyn              #
1= Cadastrar
2= Listar
0= Sair
qual opçao?
========== RESTART: D:/curso python ketlyn/Aula 4/aula 4 estoque.py ==========

========== RESTART: D:/curso python ketlyn/Aula 4/aula 4 estoque.py ==========
>>> 
========== RESTART: D:/curso python ketlyn/Aula 4/aula 4 estoque.py ==========
>>> 
========== RESTART: D:/curso python ketlyn/Aula 4/aula 4 estoque.py ==========
######## Magazine da Maria ########
 Sistema de Controle de Estoque-Versao 1.0#
#   Desenvolvido por: Ketlyn              #
1= Cadastrar
2= Listar
3= apagar
0= Sair
qual opçao?4
opçao invalida
######## Magazine da Maria ########
 Sistema de Controle de Estoque-Versao 1.0#
#   Desenvolvido por: Ketlyn              #
1= Cadastrar
2= Listar
3= apagar
0= Sair
qual opçao?3
Traceback (most recent call last):
  File "D:/curso python ketlyn/Aula 4/aula 4 estoque.py", line 65, in <module>
    menu()
  File "D:/curso python ketlyn/Aula 4/aula 4 estoque.py", line 28, in menu
    apagar()
NameError: name 'apagar' is not defined
>>> 
========== RESTART: D:/curso python ketlyn/Aula 4/aula 4 estoque.py ==========
######## Magazine da Maria ########
 Sistema de Controle de Estoque-Versao 1.0#
#   Desenvolvido por: Ketlyn              #
1= Cadastrar
2= Listar
3= apagar
0= Sair
qual opçao?4
opçao invalida
######## Magazine da Maria ########
 Sistema de Controle de Estoque-Versao 1.0#
#   Desenvolvido por: Ketlyn              #
1= Cadastrar
2= Listar
3= apagar
0= Sair
qual opçao?3
######## Magazine da Maria ########
 Sistema de Controle de Estoque-Versao 1.0#
#   Desenvolvido por: Ketlyn              #
1= Cadastrar
2= Listar
3= apagar
0= Sair
qual opçao?3
######## Magazine da Maria ########
 Sistema de Controle de Estoque-Versao 1.0#
#   Desenvolvido por: Ketlyn              #
1= Cadastrar
2= Listar
3= apagar
0= Sair
qual opçao?
========== RESTART: D:/curso python ketlyn/Aula 4/aula 4 estoque.py ==========
######## Magazine da Maria ########
 Sistema de Controle de Estoque-Versao 1.0#
#   Desenvolvido por: Ketlyn              #
1= Cadastrar
2= Listar
3= apagar
0= Sair
qual opçao?1
digite o nome do produto:tv
digite a quantidades:5
Quer continuar?(S)im ou (N)ao:tv
######## Magazine da Maria ########
 Sistema de Controle de Estoque-Versao 1.0#
#   Desenvolvido por: Ketlyn              #
1= Cadastrar
2= Listar
3= apagar
0= Sair
qual opçao?1
digite o nome do produto:tv
produto ja cadastrado!
digite o nome do produto:
