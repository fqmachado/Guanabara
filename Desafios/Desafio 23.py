# Desafio 23:
# Um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados, identificando-os por:
# Unidade, dezenena, centenar, milhar.

# TRabalhando como string:

num = str(input('Digite um número de 0 a 9999: '))
print('Milhar: {}'.format(num[0]))
print('Centena: {}'.format(num[1]))
print('Dezena: {}'.format(num[2]))
print('Unidade: {}'.format(num[3]))

# Fiz pela segunda vez.




"""
numero = int(input('Informe um número de 0 a 9999: '))
num = str(numero)
print('Analisando o número {}'.format(num))
print('Milhar: {}'.format(num[0]))
print('Centena: {}'.format(num[1]))
print('Dezena: {}'.format(num[2]))
print('Unidade: {}'.format(num[3]))
"""

# Trabalhando como númnero: (matematicamente porque não estamos usando estruturas de repetição ainda).
numero = int(input('Informe um número de 0 a 9999: '))
print('Analisando o número {}'.format(numero))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000
print('Milhar: {}'.format(m))
print('Centena: {}'.format(c))
print('Dezena: {}'.format(d))
print('Unidade: {}'.format(u))
