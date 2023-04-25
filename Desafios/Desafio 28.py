# Desafio 28 - Adivinhação
# Programa que faça o computador 'pensar' em um número inteiro de 0 a 5.
# E que peça ao usuário para tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

"""
# Como eu fiz:
import random
num = int(input('Digite um número inteiro de 0 a 5: '))
x = random.randint(0,5)  # Faz o computador 'pensar'.
if num == x:
    print('Você escolheu o mesmo número que o computador, que é {}. Então você venceu! Parabéns!'.format(x))
else:
    print('Que pena... Você perdeu :(')
print(x)
"""

# Como o Guanabara fez:
from random import randint
from time import sleep   # importa o módluo sleep, para fazer o programa parar pelos segundos escolhidos.
computador = randint(0,5)
print('-=-' * 20)
print('Pensei em um número entre 0 e 5. Vamos ver se você adivinha qual é...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)         # Faz o programa parar a execução por x segundos.
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer ! ')
else:
    print('GANHEI! Eu pensei no número {} e não no {}.'.format(computador, jogador))