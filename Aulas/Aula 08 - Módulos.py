"""
Aula 08
Utilizando Módulos.


Podemos importar uma biblioteca inteira ou apenas módulos, que correspondem a funcionalidades:
Ex de Biblioteca inteira: import math
Ex de módulo: from math import sqrt (módulo de raiz quadrada)
              from math import sqrt, ceil (raiz quadrada e arredondamento para cima)


IMPORTANDO TODA A BIBLIOTECA:
# Primeiro é preciso importar a biblioteca para que as funcionalidades sejam importadas:
# Ex com a função sqrt com arredondamento para 2 casas decimais (2a chave do print).
import math
num = int(input('Digite um número:'))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}.'.format(num, raiz))

# Ex com a função ceil:
import math
num = int(input('Digite um número:'))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}.'.format(num, math.ceil(raiz)))


# IMPORTANDO MÓDULOS:
# Ex1
from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num) # note que aqui usei diretamente a função sqrt, pois importei apenas o módulo sqrt.
print('A raiz quadrada de {} é igual a {}.'.format(num, raiz))

# Ex2:
from math import sqrt, floor
num = int(input('Digite um número:'))
raiz = sqrt(num)
print('A raiz quadrada de {} é igual a {:.2f}.'.format(num, floor(raiz))) # floor sem math.floor, pois foi
# importada apenas o módulo.


# Ex de biblioteca RANDOM
# Ex de comando random puro
import random
num = random.random() # geraa um número aleatório entre 0 e 1.
print(num)

# Ex de comando random específico, com uma faixa.
import random
num = random.randint(1, 10) # geraa um número aleatório entre 0 e 1.
print(num)

import emoji
print(emoji.emojize("Meu veículo preferido é :speedboat:"))


# DESAFIOS
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


# Desafio 17:
# Um programa que leia os comprimentos dos catetos de um triângulo retângulo, e calcule e mostre o
# comprimento da hipotenusa.

# Um método tradicional, que é usando a fórmula h2 = o2 + a2
from math import sqrt
o = float(input('Cateto oposto: '))
a = float(input('Cateto adjacente: '))
h = sqrt((o**2) + (a**2))
print('Hipotenusa = {:.2f}.'.format(h))

# Agora, um método pythônico:
from math import hypot
o = float(input('Cateto oposto: '))
a = float(input('Cateto adjacente: '))
print('Hipotenusa: {:.2f}.'.format(hypot(o, a)))

from math import hypot
o = float(input('Cateto oposto: '))
a = float(input('Cateto adjacente: '))
h = hypot(o, a)
print('Hipotenusa: {:.2f}.'.format(h))


# Desafio 18:
# Programa que leia um ângulo qualquer e mostre na tela o seno, cosseno e a tangente deste ângulo.

import math
a = float(input('Informe um ângulo: '))
print('Um ângulo de {:.2f}graus tem seno={:.2f}, cosseno={:.2f} e tangenge ={:.2f}.'.format(a, math.sin(a), math.cos(a), math.tan(a)))


"""

# Desafio 19:
# Programa que ajude a sortear um de seus 4 alunos para apagar o quadro, lendo os nomes deles e escrevendo
# o nome escolhido.

a = str(input('Aluno 1: '))
b = str(input('Aluno 2: '))
c = str(input('Aluno 3: '))
d = str(input('Aluno 4: '))
import random
nome = random.choice(a, d)
print(nome)


