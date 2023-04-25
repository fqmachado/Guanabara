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

