#estoque.py

produto = input('digite o nome do produto:')
preco = float(input('digite o preço:'))
quantidade = int(input('digite a quantidade:'))
total=preco*quantidade

#informar produto,preço e quantidade
print('nome do produto:', produto)
print('preço do produto R$',preco)
print('quantidade:',quantidade)
print('total em estoque R$ %.2f' % total)

