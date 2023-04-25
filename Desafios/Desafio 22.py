# Desfio 22
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# a) O nome com todas as letras maiúsculas
# b) O nome com todas minúsculas.
# c) Quantas letras ao todo (sem considerar espaços)
# d) Quantas letras tem o primeiro nome.

nome = str(input('Nome completo: '))
print('Seu nome em maiúsculas é {}.'.format(nome.upper()))
print('Seu nome em minúsculas é {}.'.format(nome.lower()))
print('Seu nome tem {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu prieiro nome tem {} letras.'.format(nome.find(' ')))
# Outra forma de fazer:
print('Seu primeiro nome é {} e tem {} letras.'.format(nome.split()[0], len(nome.split()[0])))

# Feito pela seguunda vez.





nome = str(input('Digite um nome completo: ')).strip() # o strip sem l ou r elimina os espaços à dir e à esq da string.
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(nome.find(' '))) # comando curto, mas difícil de entender.
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0]))) #comando maior, mas mais fácil de entender.










