"""
Lembrete do curso da Udemy:

FATIAMENTO (SLICING)
Ex:
        [ 0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20
 nome = ['C' 'u' 'r' 's' 'o' ' ' 'e' 'm' ' ' 'V' 'i' 'd' 'e' 'o' ' ' 'P' 'y' 't' 'h' 'o' 'n']

> SE faço nome[5], ele vai buscar o caractere da posição 5.
> Mas se faço nome[0:3], ele vai buscar o caractere da pos 0 até a pos 2, ou seja, desconsidera a posição final
informada.
> E se faço [:3], ele fará a mesma coisa.
> De forma análoga, [1:] buscará todos os caracteres de 1 até o último, que no caso é 5.

> Outra forma de slicing: [9::3] > Assim, mostramos os caracteres a partir da posição 9 variando de 3 em 3.
Neste exemplo, ele mostraria: V,e,P,h.


ANÁLISE
Dá para saber várias info de um string, como: qual é o seu tamanho, com que letra ela termina, etc.
Por ex: a Função LEN ( do inlês length) mostra o tamanho, o comprimento de uma frase.



frase = 'Curso em Video Python'
print(frase.count('o')) # Conta quantas vezes a letra 'o' aparece na string.
print(frase[9::3]) # Começa no caractere 9 e vai até o final de 3 em 3.
print(frase[9:]) # Começa no caractere 9 e vai até o final identificando todos.

# ANÁLISE
# Analisar uma string é saber algumas informações sobre ela (com qual letra começa, com qual termina, tamanho, etc)

# função LEN
print(len(frase))

# Função COUNT
print(frase.count('o'))
print(frase.count('o',0,13)) # conta quantas letras 'o' existem de 0 a 12 (que é o 13-1)

# Função FIND
# Temos o find e também o rfind, que procura na string a partir do seu lado direito.
print(frase.find('deo')) # encontra o pedaço de trecho procurado e informa o momento em que ele começou.
# No caso desse exemplo, o deo começou no caractere 11.
# Agora, um exemplo de quando há erro:
print(frase.find('Android')) # retorna -1 porque foi procurada uma string que não existe.
# Operador in
print('Curso'in frase) # procurando uma palavra específica dentro da string.
O resultado neste caso é false.

# TRANSFORMAÇÃO
print(frase.replace('Phython','Android'))
print(frase.upper()) # transforma todas as letras em maiúsculas.
print(frase.lower()) # transforma todas as letras em minúsculas.
print(frase.capitalize()) # Pega o string inteiro e deixa em maiúsculo apenas a 1a letra da 1a palavra.
print(frase.title()) # FAz o capitalize palavra por palavra.


# Usando uma string especial com espaços vazios nas extremidades.
frase = '   Aprenda Python  '
print(frase)
print(frase.strip()) # strip remove os espaços vazios nas extremidades.
print(frase.rstrip()) # rstrip remove os espaços vazios à direita da string.
print(frase.lstrip()) # lstrip remove os espaços vazios à esquerda da string.


# Mais conceitos tendo a string'Curso em Video Python' como exemplo.
frase = 'Curso em Video Python'
# Comando SPLIT = split gera uma lista com todas as palavras de uma dada cadeia de caracteres.
# Temos o split e o rsplit, que começa a enumerar as novas strings a partir da direita da cadeia.
print(frase.split())
print('-'.join(frase)) # insere o caractere entre aspas entre as letras da string.



"""



frase = 'Curso em Video Python'
print(frase[1:15:2]) # Imprime do caractere 1 ao 15, de 2 em 2.

# Para imprimir textos longos como o abaixo, não é preciso dar um print em cada linha.
# Basta delimitar o texto com """ no comando print. Veja:
print("""Welcome! Are you completely new to programming?
If not, then we presume you will be looking for information
about why and how to get started with not Python""")

print(frase.upper().count('O')) # maneira de combinar comandos. Aqui, passou a ter 'O', e então os 'O'foram contados.
print(frase.replace('Python', 'Android'))

# IMPORTANTE:
# Uma string é imutável, a não ser que eu utilize uma função de transformação de string (ex: replace) e faça
# uma atribuição, isto é, a salve já transformada, como por exemplo dentro do mesmo nome da string original.
# Ex:
frase.replace('Phython', 'Android')
print(frase) # não vai imprimir porque a mudança não foi salva.

# Para imprimir já alterado, o correto é:
frase = frase.replace('Phython', 'Android')
print(frase) # (Verificar por que não funcionou )

dividido = frase.split()
print(dividido)
print(dividido[2][3])


# Os desafios desta unidade vão do 22 ao 27.













