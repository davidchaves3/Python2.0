print("-=-"*20)
salario = float(input("Qual seu salário R$"))
print("-=-"*20)
if salario > 1250 :
  print("-=-"*20)
  print(f"Seu aumento é de {salario*0.10} e seu salário será de {salario + (salario*0.10)}")
  print("-=-"*20)
else:
  print("-=-"*20)
  print(f"Seu aumento é de {salario*0.15} e seu salário será de {salario + (salario*0.15)}")
  print("-=-"*20)