# Item 9
estado = input("Digite a sigla do seu estado (ex: RJ, SP, MG): ").upper()

if estado == "RJ":
    print("Carioca")
elif estado == "SP":
    print("Paulista")
elif estado == "MG":
    print("Mineiro")
else:
    print("Outro estado")