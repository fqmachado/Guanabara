# Desafio 16:
# Um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira.

from math import trunc
n = float(input('Digite um número real: '))
print("A parte inteira deste número é {}.".format(trunc(n)))
# ou a opção de importar toda a biblioteca:
import math
n = float(input('Digite um número real: '))
print("A parte inteira deste número é {}.".format(math.trunc(n)))
# Outra forma, sem importar a biblioteca math, é:
n = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua parte inteira é {}.'.format(n, int(n)))
