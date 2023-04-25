# Desafio 26
# Programa que leia uma frase pelo teclado e mostre:
# > Quantas vezes aparece a letra A.
# > Em que posição ela aparece pela primeira vez.
# > Em que posição ela aparece pela última vez.

frase = str(input('Digite uma frase:'))
print('A letra A aparece {} vezes.'.format(frase.upper().count('A')))
print('A letra A aparece pela primeira vez na posição {}.'.format(frase.upper().find('A')))
print('A letra A aparece pela última vez ns posição {}.'.format(frase.upper().rfind('A')))








frase = str(input('Frase do dia: ')).strip()
print('A sua frase tem {} letras A.'.format(frase.upper().count('A')))
print('A primeira letra A apareceu na posição {}.'.format(frase.find('A')))
print('A última letra A apareceu na posição {}.'.format(frase.rfind('A')))


#Posso também fazer assim:
# frase = str(input('Frase do dia: ')).strip().upper()
# print('A sua frase tem {} letras a.'.format(frase.count('A')))






