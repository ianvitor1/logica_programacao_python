# Item 8
maiores_de_idade = 0

for _ in range(10):
    idade = int(input("Digite a idade: "))
    if idade >= 18:
        maiores_de_idade += 1

print(f"A quantidade de pessoas maiores de idade é: {maiores_de_idade}")
