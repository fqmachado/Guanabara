# DEsafio 32
# Um programa que leia um ano e informe se ele é BISSEXTO.

# Para o usuário digitar o ano pretendido para análise:
"""
ano = int(input("Informe um ano, e eu te informarei se ele é bissexto ou não: "))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano BISSEXTO.')
else:
    print('Ano NÃO-BISSEXTO')
"""

# Para analisar o ano atual:
from datetime import date
ano = int(input('Informe um ano para saber se ele é ou não bissexto:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO.'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO.'.format(ano))

