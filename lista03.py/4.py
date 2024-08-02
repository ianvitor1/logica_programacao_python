def calcular_idade(ano_corrente, ano_nascimento):
    idade = ano_corrente - ano_nascimento
    return idade

# Exemplo de uso
ano_corrente = 2023  # Você pode usar a função datetime para obter o ano atual
ano_nascimento = int(input("Digite o seu ano de nascimento: "))
idade = calcular_idade(ano_corrente, ano_nascimento)
print(f"Sua idade é: {idade} anos.")