# Desafio 12:
# Algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

preço = float(input('Preço do produto:'))
desc = preço * 0.95
print('Com desconto de 5%, este produto custa R${}.'.format(desc))

