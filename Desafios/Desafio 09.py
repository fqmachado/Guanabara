# Desafio 09
# Leia um número inteiro qualquer e mostre na tela a sua tabuada.
# Abaixo está uma forma nada pythônica, com a linha de código indo muito além do campo visual da tela:
"""n = int(input('INforme um número inteiro:'))
a = n*1
b = n*2
c = n*3
d = n*4
e = n*5
f = n*6
g = n*7
h = n*8
i = n*9
j = n*10
print('A tabuada desse número é a seguinte: \n {} x 1 = {} \n {} x 2 = {} \n {} x 3 = {} \n {} x 4 = {} \n {} x 5 = {} \n {} x 6 = {} \n {} x 7 = {} \n {} x 8 = {} \n {} x 9 = {} \n {} x 10 = {}'.format(n,a,n,b,n,c,n,d,n,e,n,f,n,g,n,h,n,i,n,j))
"""

"""
# Abaixo, uma forma melhor organizada, mas também longa:
num = int(input('Digite um número para ver a sua tabuada: '))
print('_' * 12)              # comando para repetir o underscore (_) 12 vezes, e criar uma linha pontilhada.
print('{} x {:2} = {}'.format(num, 1, num * 1))     # o comando {:2} desloca o dado em 1 casa para a direita, para organizar.
print('{} x {:2} = {}'.format(num, 2, num * 2))
print('{} x {:2} = {}'.format(num, 3, num * 3))
print('{} x {:2} = {}'.format(num, 4, num * 4))
print('{} x {:2} = {}'.format(num, 5, num * 5))
print('{} x {:2} = {}'.format(num, 6, num * 6))
print('{} x {:2} = {}'.format(num, 7, num * 7))
print('{} x {:2} = {}'.format(num, 8, num * 8))
print('{} x {:2} = {}'.format(num, 9, num * 9))
print('{} x {} = {}'.format(num, 10, num *10))
print('_' * 12)
"""

# Agora, uma forma pythônica, usando estruturas de repetição:
num = int(input('Digite um número para saber sua tabuada: '))
c = 1
while c < 11:
    print('{} x {} = {}'.format(num, c, num * c))
    c = c + 1
