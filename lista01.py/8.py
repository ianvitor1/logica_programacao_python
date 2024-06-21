# Item 8
ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

if ano_nascimento > 0 and ano_nascimento <= ano_atual:
    idade = ano_atual - ano_nascimento
    print("A idade da pessoa é:", idade)
else:
    print("Ano de nascimento inválido")