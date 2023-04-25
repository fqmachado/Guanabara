# Desafio 29
# Programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostrar uma mensagem dizendo que ele foi multado.
# A multa custa R$7,00 por cada Km/h excedente.


vel = int(input('Informe a velocidade atual do veículo: '))
multa = (vel-80) * 7
if vel > 80:
    print('Você excedeu o limite de velocidade. Será multado em R${:.2f}'.format(multa))
else:
    print('Parabéns! Você é um motorista prudente.')
    print('Tenha um bom dia. Dirija com segurança.')

