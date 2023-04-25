# Desafio 34
# Programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a 1250: aumento de 10%.
# Para salários inferiores ou iguais a 1250: aumento de 15%.


sal = float(input('Informe o salário do funcionário: '))
from time import sleep
sleep(2)
a = sal * 1.1
b = sal * 1.15
if sal > 1250:
    print('O seu salário atualmente é R${:.2f} e passará para R${:.2f}.'.format(sal, a))
else:
    print('O seu salário atualmente é R${:.2f} e passará para R${:.2f}.'.format(sal, b))

