# Item 12
altura = float(input("Digite a altura (em metros): "))
sexo = input("Digite o sexo (M para masculino, F para feminino): ").upper()

if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
    print("O peso ideal para um homem de", altura, "m é:", peso_ideal, "kg")
elif sexo == "F":
    peso_ideal = (62.1 * altura) - 44
    print("O peso ideal para uma mulher de", altura, "m é:", peso_ideal, "kg")
else:
    print("Sexo inválido")
