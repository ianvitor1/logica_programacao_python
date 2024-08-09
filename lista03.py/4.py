def calcular_idade(ano_corrente, ano_nascimento):
    idade = ano_corrente - ano_nascimento
    return idade

ano_corrente = 2023
ano_nascimento = int(input("Digite o seu ano de nascimento: "))
idade = calcular_idade(ano_corrente, ano_nascimento)
print(f"Sua idade é: {idade} anos.")