def tabuada(numero):
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Exemplo de uso da função
numero = int(input("Digite um número para ver a tabuada: "))
tabuada(numero)