# Desafio 24
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra SANTO.

cidade = str(input("Nome da cidade: "))
spl = cidade.split()

print('SANTO' in spl[0].upper())

# Feito pela segunda vez.














cidade = str(input("Em que cidade você nasceu? ")).strip()
print('Analisando {}... '.format(cidade))
print(cidade[:5].upper() == 'SANTO')
