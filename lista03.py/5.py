# Lista global
numeros = [1, 2, 3, 4, 2, 5, 2, 6, 7, 8, 2]

def contar_ocorrencias(valor):
    """Função que conta quantas vezes um valor aparece na lista global."""
    return numeros.count(valor)

numero_para_verificar = int(input("Digite um número inteiro para verificar quantas vezes ele aparece na lista: "))
quantidade = contar_ocorrencias(numero_para_verificar)
print(f"O número {numero_para_verificar} aparece {quantidade} vezes na lista.")