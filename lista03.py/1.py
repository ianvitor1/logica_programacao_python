numeros = []
indices = 0
numero = int(input('Digite um numero: '))
numeros.append(numero)
maior = numero
for n in range(0,10):
    numero = int(input('Digite um numero: '))
    numeros.append(numero)
    if maior < numero:
        maior = numero
        indice = n
print(f'lista dos numeros: {numeros}')
print(f'maior numero: {maior} - seu indice é: {indice}')