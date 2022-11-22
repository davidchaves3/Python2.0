distancia = float(input("Qual a distância da viagem em KM: "))

if distancia <= 200:
  custo = distancia * 0.50
else:
  custo = distancia * 0.45
print(f"Custo da sua viagem é {custo}")