num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))

menor = num1
if num2 < num3 and num2< num1:
  menor = num2
if num3 < num1 and num3< num2:
  menor = num3

maior = num1
if num2 > num2 and num2 > num3:
  maior = num2
if num3 > num1 and num3 > num2:
  maior = num3
print(f"O menor valor é {menor}")
print(f"Maior valor é {maior}")