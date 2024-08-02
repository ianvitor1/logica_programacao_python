# Item 10
alturas = []
alturas_mulheres = []
numero_homens = 0

for _ in range(15):
    altura = float(input("Digite a altura (em metros): "))
    sexo = input("Digite o sexo (M para masculino, F para feminino): ").upper()
    
    alturas.append(altura)
    
    if sexo == "F":
        alturas_mulheres.append(altura)
    elif sexo == "M":
        numero_homens += 1

maior_altura = max(alturas)
menor_altura = min(alturas)
media_altura_mulheres = sum(alturas_mulheres) / len(alturas_mulheres) if alturas_mulheres else 0

print(f"A maior altura do grupo é: {maior_altura} m")
print(f"A menor altura do grupo é: {menor_altura} m")
print(f"A média de altura das mulheres é: {media_altura_mulheres:.2f} m")
print(f"O número de homens é: {numero_homens}")
# Item 10
alturas = []
alturas_mulheres = []
numero_homens = 0

for _ in range(15):
    altura = float(input("Digite a altura (em metros): "))
    sexo = input("Digite o sexo (M para masculino, F para feminino): ").upper()
    
    alturas.append(altura)
    
    if sexo == "F":
        alturas_mulheres.append(altura)
    elif sexo == "M":
        numero_homens += 1

maior_altura = max(alturas)
menor_altura = min(alturas)
media_altura_mulheres = sum(alturas_mulheres) / len(alturas_mulheres) if alturas_mulheres else 0

print(f"A maior altura do grupo é: {maior_altura} m")
print(f"A menor altura do grupo é: {menor_altura} m")
print(f"A média de altura das mulheres é: {media_altura_mulheres:.2f} m")
print(f"O número de homens é: {numero_homens}")