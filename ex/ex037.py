binario = []

num = int(input("Digite um número inteiro:"))

resto = num%2
quociente = num//2
binario.append(resto)

while quociente != 1 :
  resto = quociente % 2
  quociente = quociente // 2
  binario.append(resto)
  if quociente == 1 :
    binario.append(quociente)

print("Número em Binário")
print(binario[::-1])