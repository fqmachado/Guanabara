# Desafio 11:
# Programa que leia a largura e altura de uma parede, calcule a área e a qtd de tinta para pintá-lo,
# sabendo que cada litro de tinta pinta uma área de 2m quadrados.

largura = float(input('Informe a largura da parede:'))
altura = float(input('Informe a altura da parede:'))
area = largura * altura
tinta = area / 2
print('Para pintar essa parede, são necessários {:.2f}l de tinta.'.format(tinta))