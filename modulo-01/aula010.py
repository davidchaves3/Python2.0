#Condições Simples e composta ( Parte 1) - if & else

#Exemplo  de condição simples
nome = str(input('Qual é seu nome?'))
if nome == 'David':
  print('Que nome lindo você tem!')
print(f'Bom dia{nome}')

#Exemplo de condição composta
nome = str(input('Qual é seu nome?'))
if nome == 'David': # Se o nome for igual a David 
  print('Que nome lindo você tem!') # Mostre "Que nome Lindo Você tem!"
else: # Senão 
  print(f'Seu nome é tão normal!') # Mostre "Seu nome é tão normal!"
print(f'Bom dia{nome}')

#Condição simplificada 

n1 = float(input('Digite a 1ª nota:'))
n2 = float(input('Digite a 2ª nota:'))
m = (n1 + n2)/2
print(f'Sua média foi{m}')
print('PARABÉNS' if m >= 6 else ' ESTUDE MAIS!')