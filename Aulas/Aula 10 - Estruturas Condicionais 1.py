"""
Todos os 27 exercícios fietos até agora foram sequenciais, sem opções a seguir.
Com as condicionantes, isso muda.

Numa condição, é executado um bloco verdadeiro ou um bloco falso; nunca os dois.


tempo = int(input('Quantos anos tem seu carro? '))
print('Carro Novo' if tempo <= 3 else 'carro velho')
print('--FIM--')

# Exemplo simples:
nome = str(input('Qual é o seu nome?'))
if nome == 'Fabio':           # Atenção aqui para as aspas delimitando Fabio, pois a entrada é uma string.
    print('Que nome lindo! ')
    print('Bom dia, {}'.format(nome))
else:
    print("Que nome feio :( ")
#Quando não tem o ELSE, a estrutura de condicional é simples. Quanto tem ELSE, é uma estrutura COMPOSTA.


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A média das notas é {:.1f}.'.format(m))
# Condição composta:
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS ! ')
else:
    print('Sua média foi ruim. Estude mais.')
print('Bons estudos! ')


"""



# Condição simplificada:
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A média das notas é {:.1f}.'.format(m))
print('PARABÉNS' if m >= 6.0 else 'ESTUDE MAIS.')

# Os desafios vão do 28 ao 35


