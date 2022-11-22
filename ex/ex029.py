vel = float(input('Digite a velocidade km/h do carro:'))

if vel > 80 :
  multa = (vel - 80) * 7
  print("Você foi MULTADO")
  print(f"Sua multa é de {multa}")

print('Tenha um bom dia! Dirija com Cuidado!')