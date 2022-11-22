nome = input("Digite seu Nome Completo:")
print(f"Seu nome em maiúsculos é {nome.upper()}")
print(f"Seu nome em minúsculo é{nome.lower()}")
print(f"Seu nome tem ao todo {len(len(nome) - nome.count(' '))} letras")
# print(f"Seu primeiro nome tem {nome.find(' ')}
separar = nome.split()
print(f"Seu primeiro nome é{separar[0]} e ele tem {len(separar[0])}letras")