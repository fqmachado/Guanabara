# Desafio 33
# Um programa que leia 03 números e mostre qual é o maior e qual é o menor.

a = float(input('1º número: '))
b = float(input('2º número: '))
c = float(input('3º número: '))
menor = 0
maior = 0
# Verificando quem é o menor:
if a<b and a<c:
    menor = a
if b<c and b<a:
    menor = b
if c<b and c<a:
    menor = c

# Verificando quem é o maior:
if a>b and a>c:
    maior = a
if b>c and b>a:
    maior = b
if c>b and c>a:
    maior = c

print('O menor número é {}.'.format(menor))
print('O maior número é {}.'.format(maior))
