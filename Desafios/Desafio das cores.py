# Desafio 30 com cores
# Um programa que leia um número inteiro e mostre se ele é par ou ímpar.

"""
num = int(input('Digite um número inteiro:'))
if num % 2 == 0:
    print('O número \033[4;32m{}\033[m é par.'.format(num))
else:
    print('O número \033[4;31m{}\033[m é ímpar.'.format(num))
"""


"""
# Desafio 28 com  cores: Adivinhação
from random import randint
from time import sleep
print('\033[1;33m-=-\033[m'*20)
print('\033[1;36mJogo da adivinhação\033[m')
print('\033[1;33m-=-\033[m'*20)
computador = randint(0,5)
eu = int(input('Pensei em um número entre 0 e 5. \033[1;31mVamos ver se você adivinha qual foi... :\033[m'))
if eu == computador:
    print('\033[1;34mVocê acertou!\033[m')
else:
    print('Você errou. Eu pensei foi no \033[4;31m{}\033[m e não no \033[4;34m{}\033[m.'.format(computador, eu))
"""

"""
# Desafio 27 - separando nome e sobrenome.
# Programa que leia o nome completo, e mostre em seguida o primeiro e o último nome separadamente,
# independentemente da quantidade de sobrenomes.


n = str(input('Nome completo: '))
nome = n.split()
print('Seu primeiro nome é \033[1;35m{}\033[m.'.format(nome[0]))
print('Seu último sobrenome é \033[1;37m{}\033[m.'.format(nome[len(nome)-1]))
"""

# Desafio 06
# Um algoritmo que leia um número e mostre o seu dobro, seu triplo e sua raiz quadrada.

n = int(input('Informe um número: '))
print('O número \033[4;37m{}\033[m tem como dobro \033[4;31m{}\033[m, triplo \033[4;34m{}\033[m e raíz quadrada \033[4;35m{}\033[m.'.format(n, n*2, n*3, n**(1/2)))


