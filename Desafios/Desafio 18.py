# Desafio 18:
# Programa que leia um ângulo qualquer e mostre na tela o seno, cosseno e a tangente deste ângulo.

import math
a = float(input('Informe um ângulo: '))
print('Um ângulo de {:.2f}graus tem seno={:.2f}, cosseno={:.2f} e tangenge ={:.2f}.'.format(a, math.sin(a), math.cos(a), math.tan(a)))
