'''
Algoritmo que armazena uma lista de nomes. O usuário
deve digitar os nomes até que seja informado o valor -1.
Mostrar o número de pessoas
Printar a lista de ordem alfabética
Printar o 3º elemento da lista
Realizar um sorteio e mostrar o nome do ganhador
'''

import random
nomes = []
while True:
    nome = input("Digite um nome (ou -1 para sair): ")
    if nome == "-1":
        break
    else:
        nomes.append(nome)

print(f"Número das pessoas: {len(nomes)}")
print(f"Lista de nomes: {nomes}")
nomesOrdenados = sorted(nomes)
print(f"Lista de nomes em ordem alfabética: {nomesOrdenados}")

print(f'O terceiro nome ordenado é {nomes[2]}')

random.seed()
sorteado = random.randint(0, len(nomes)-1)
print(f'O nome sorteado foi: {nomes[sorteado]}')