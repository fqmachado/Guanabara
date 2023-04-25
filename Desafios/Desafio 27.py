# Desafio 27
# Programa que leia o nome completo, e mostre em seguida o primeiro e o último nome separadamente,
# independentemente da quantidade de sobrenomes.

n = str(input('Nome completo: ')).strip()
print('Muito prazer em te conhecer!')
nome = n.split()
print('Seu primeiro nome é {}.'.format(nome[0]))
print('Seu último sobrenome é {}.'.format(nome[len(nome)-1]))








