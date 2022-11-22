reta1 = float(input("Digite o comprimento da 1ª reta:"))
reta2 = float(input("Digite o comprimento da 2ª reta:"))
reta3 = float(input("Digite o comprimento da 3ª reta:"))

if reta1  < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
  print("É possível montar um triângulo")
else:
  print("Não pode ser feitp um triângulo")
  