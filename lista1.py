# Item 1
numero = float(input("Digite um número: "))
if numero > 20:
    print("O número é maior que 20:", numero)
# Item 2
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
soma = numero1 + numero2
if soma > 10:
    print("A soma é maior que 10:", soma)
# Item 3
import math

numero = float(input("Digite um número: "))
if numero >= 0:
    print("A raiz quadrada do número é:", math.sqrt(numero))
else:
    print("O quadrado do número é:", numero ** 2)
# Item 4
numero = int(input("Digite um número: "))
if numero % 3 == 0:
    print("É MULTIPLO DE 3")
else:
    print("NÃO É MULTIPLO DE 3")
# Item 5
numero = int(input("Digite um número: "))
if numero % 5 == 0:
    print("É MULTIPLO DE 5")
else:
    print("NÃO É MULTIPLO DE 5")
# Item 6
numero = int(input("Digite um número: "))
if numero % 3 == 0 and numero % 7 == 0:
    print("O número é divisível por 3 e por 7")
else:
    print("O número não é divisível por 3 e por 7")
# Item 7
numero = int(input("Digite um número: "))
if 20 <= numero <= 90:
    print("O número está compreendido entre 20 e 90")
else:
    print("O número não está compreendido entre 20 e 90")
# Item 8
ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

if ano_nascimento > 0 and ano_nascimento <= ano_atual:
    idade = ano_atual - ano_nascimento
    print("A idade da pessoa é:", idade)
else:
    print("Ano de nascimento inválido")
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
