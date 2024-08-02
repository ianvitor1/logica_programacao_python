# Item 3
contador = 0

while True:
    numero = float(input("Digite um número (digite um número negativo para parar): "))
    if numero < 0:
        break
    contador += 1

print("Quantidade de números digitados:", contador)
