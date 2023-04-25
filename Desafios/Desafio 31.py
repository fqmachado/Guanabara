# Desafio 31
# Programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

viagem = float(input('Informe a distância da viagem: '))
"""
if viagem > 200:
    preço = viagem * 0.45
    print('Esta viagem custa R${:.2f}.'.format(preço))
else:
    preço = viagem * 0.50
    print('Esta viagem custa R${:.2f}.'.format(preço))
"""

# Usando o IF simplificado:
viagem = float(input('Informe a distância da viagem: '))
preço = viagem * 0.50 if viagem <= 200 else viagem * 0.45
print('Esta viagem custa R${:.2f}.'.format(preço))

