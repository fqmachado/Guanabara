# Um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo.

print('-='*20)
print('Analisador de Triângulos.')
print('-='*20)

a = float(input('Informe o primeiro lado:'))
b = float(input('Informe o segundo lado:'))
c = float(input('Informe o terceiro lado:'))

if a + b > c and a + c > b and b + c > a:
    print('Podemos formar um triângulo com essas medidas.')
else:
    print('Impossível formar um triângulo.')
