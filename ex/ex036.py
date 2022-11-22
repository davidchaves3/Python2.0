print("======================EMPRSTIMO BANCÁRIO======================\n")
print("==============================================================")
valorCasa = float(input("Qual valor da casa que você deseja comprar?"))
print("==============================================================")
salario = float(input("Qual é o seu salário?"))
print("==============================================================")
anosPagar = float(input("Quantos anos você vai pagar?"))

mensalidade = valorCasa/(anosPagar * 12)

if mensalidade > salario * 0.30:
  print("==============================================================")
  print("                      EMPRESTIMO NEGADO                       ")
  print("==============================================================")
else:
  print("==============================================================")
  print("                     EMPRESTIMO APROVADO                      ")
  print("==============================================================")
  print(f"Deverá pagar uma mensalida de {mensalidade:.3}")
