"""
Aula 07
Operadores Aritméticos.

Ordem de precedência:
1- parênteses ()
2- potências **
3- * / // %, na ordem em que eles aparecerem.
4- + -

Ex:
3*5+4**2 == 31
3*(5+4)**2 == 243

# Exemplo de operações com resultado na tela:
n1 = int(input('um valor:'))
n2 = int(input('outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 //n2
p = n1 ** n2
print('A soma vale {},\n a multiplicação valie `{}, \n e a divisão vale {:.3f}'.format(s, m, d), end='') # o  end =''
# serve para fazer a linha não quebrar ao final do print, ou seja, a linha  seguinte começar logo no final da atual.
print('Div inteira = {}, \n potência = {}'.format(di, p))


# Desafio 05
# Um programa que leia um número inteiro e mostre na tela o seu sucessor e o seu antecessor.
n = int(input('Digite um número'))
print('O antecesssor deste número é {} e o sucessor é {}'.format(n-1, n+1))


# Desafio 06
# Um algoritmo que leia um número e mostre o seu dobro, seu triplo e sua raiz quadrada.
n = int(input('informe um número:'))
print('Este número tem como dobro {}, triplo {} e raíz quadrada {}'.format(n*2, n*3, n**(1/2)))


# Desafio 07
# Um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
n1 = int(input('Informe a 1a nota:'))
n2 = int(input('Informe a 2a nota:'))
print('A média das notas é {}'.format((n1+n2)/2))


# DEsafio 08
# Um programa que leia um valor em metros e o converta para cm e mm.
n = int(input('Informe a medida:'))
print('Essa medida corresponde a {}cm e {}mm'.format(n/0.01, n/0.001))


            # Monitoria: acho que não ficou pythônico

# Desafio 09
# Leia um número inteiro qualquer e mostre na tela a sua tabuada.
n = int(input('INforme um número inteiro:'))
a = n*1
b = n*2
c = n*3
d = n*4
e = n*5
f = n*6
g = n*7
h = n*8
i = n*9
j = n*10
print('A tabuada desse número é a seguinte: \n {} \n {} \n {} \n {} \n {} \n {} \n {} \n {} \n {} \n {}'.format(a,b,c,d,e,f,g,h,i,j))


# Desafio 10:
# Programa que leia quanto dinheiro a pessoa tem na carteira e mostre quandos Dólares ela pode comprar.
# Considere: R$1,00 = 5,17

real = int(input('Informe quanto você tem na carteira:'))
cambio = real * 5.17
print('Com R${:.2f} você pode comprar US${:.2f}.'.format(real, cambio))


# Desafio 11:
# Programa que leia a largura e altura de uma parede, calcule a área e a qtd de tinta para pintá-lo,
# sabendo que cada litro de tinta pinta uma área de 2m quadrados.

largura = float(input('Informe a largura da parede:'))
altura = float(input('Informe a altura da parede:'))
area = largura * altura
tinta = area / 2
print('Para pintar essa parede, são necessários {:.2f}l de tinta.'.format(tinta))


# Desafio 12:
# Algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

preço = float(input('Preço do produto:'))
desc = preço * 0.95
print('Com desconto de 5%, este produto custa R${}.'.format(desc))


# Desafio 13:
# Ler o salário de um funcionário e mostrar seu novo salário com 15% de aumento.

sal = float(input('Informe seu salário:'))
aumento = sal * 1.0589
print('Com 5.89% de aumento, seu novo salário seria R${:.2f}.'.format(aumento))

"""












