frase = 'Curso em Vídeo Python'
# Fatiar a String.
print(frase[3:13])#Vai mostra da letra que está na posição 3 até posição 12.

print(frase[::2])#Vai imprimir a letra que está na posição zero vai pular duas posições e imprimir a letra na posição 3 assim por diante.

# CONTAGEM DE OBJETOS EM UMA LISTA OU STRING.

print(frase.count('o'))# A função count() retorna a contagem de quantas vezes as letras O apareceu na Frase.

# CONVERTER A STRING PARA MAIUSCULO.

print(frase.upper)#Pega a frase inteira e colocar em caixa Alta.

#TAMANHO DA FRASE/LISTA

print(len(frase))#Retorna o tamanho da frase, até os espaços são considerados no tamanho.

#REMOVER OS ESPAÇOS/ REMOVER AS POSIÇÕES EM BRANCO.

print(len(frase.strip()))#Vai retornar o tamanho da lista mas agora não vai contabilizar os espaços em branco da frase.

#TROCAR PALAVRAS DA FRASE.

print(frase.replace('Python','Android'))#Vai trocar a Palavra PYTHON por ANDROID na frase. vai trocar somente na instâcia

#Para trocar efetivamente a string, frase = frase.replace("Python","Android")
# assim você vai está atribuindo a string.

# VERIFICAR SE A PALAVRA NA STRING.

print('Curso' in frase)#Se vai palavra curso Tiver na frase ele irá retorna TRUE senão vai retorna FALSE.

print(frase.find('Curso'))
#O find irá retorna em qual posição está a palavra CURSO.

# DIVIDIR A STRING PELO OS ESPAÇOS

print(frase.split())
#Vai separar a STRING e cada Palavra sera sub-frase com suas posições