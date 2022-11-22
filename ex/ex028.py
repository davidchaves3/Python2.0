import random as r
from time import sleep 

sorteado = r.randrange(0 , 5)
print('-=-'*20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print('-=-'*20)
resposta = int(input('Em que número eu pensei!?'))
print("PROCESSANDO.....")
sleep(3)
if sorteado == resposta:
  print(f'Você acertou! Parabéns!')
else:
  print(f'Você ERROU! O Número era {sorteado}')