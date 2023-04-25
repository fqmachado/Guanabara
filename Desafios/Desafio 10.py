# Desafio 10:
# Programa que leia quanto dinheiro a pessoa tem na carteira e mostre quandos Dólares ela pode comprar.
# Considere: R$1,00 = 5,17

real = int(input('Informe quanto você tem na carteira:'))
cambio = real * 5.17
print('Com R${:.2f} você pode comprar US${:.2f}.'.format(real, cambio))