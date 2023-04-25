# Cores no Terminal.
# ir para o caminho D:\Sandisk nano\Python\Prints de aulas  e abrir o arquivo que tem os códigos de cores e estilos.

# Sintaxe básica: \033[ m], onde entre o [ e o m devemos informar os códigos de estilo, texto e fundo.

print('Olá mundo!') # sem nenhum código para estilo, texto e fundo.

print('\033[1;33;44mOlá, mundo!\033[m') # estilo negrito, texto amarelo e fundo azul.
# Agora, invertendo ascores de texto e fundo:
print('\033[7;33;44mOlá, mundo"\033[m') # estilo invertido, e cores de texto e fundo azul invertidas.

# Agora, exemplo de exibição de resultados com cores diferenes:
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a, b))

# Agora, inserindo códigos mais curtos para cores:
nome = 'Machado'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))
