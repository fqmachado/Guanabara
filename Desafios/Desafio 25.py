# Desafio 25:
# Programa que leia o nome completo de uma pessoa e diga se ela tem SILVA no nome.


nome = str(input('Digite o nome completo: '))
print('SILVA' in nome.upper())


# Feito pela segunda vez.










nome = str(input('Nome completo: ')).strip()
print('Analisando {}...'.format(nome))
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))


