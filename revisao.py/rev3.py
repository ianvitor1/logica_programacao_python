total = 0
produtos = []
qtdes = []
precos = []
while True:
    produto = input('Produto: ')
    produtos.append(produto)
    qtde = int(input('Quantidade: '))
    qtdes.append(qtde)
    preco = float(input('Preço: '))
    precos.append(precos)
    total = total + qtde * preco

    s = input('Digite s para sair ou enter para continuar: ')
    if s.upper() == 'S':
        break
print('######### Itens da compra ###########')
for i in range(len(produtos)):
    print(f'Item {i+1}: {produtos[i]} - {qtdes[i]} * {precos[i]} = {qtdes[i]*precos[i]}')

print(f'Total da compra: {total}')

print('\n############## Formas de Pagamento ############')
print('1- A vista em dinheiro ou cheque' )
print('2- A vista no cartao de credito' )
print('3- Em duas vezes no cartão de crédito')
print('4- Em tres vezes no cartão de crédito, juros de 10%')

condicao = int(input('Código Condição de pagamento: '))

if condicao == 1:
    total_a_pagar = total - 10/100 * total
    print(f'Total a pagar com 10% de desconto: {total_a_pagar}')
elif condicao == 2:
    total_a_pagar = total - 15/100 * total
    print(f'Total a pagar com 15% de desconto: {total_a_pagar}')
elif condicao == 3:
    total_a_pagar = round(total / 2, 2)
    print(f'Total a pagar 2x de: {total_a_pagar}')
elif condicao == 4:
    total_a_pagar = total + 10/100 * total
    total_a_pagar = round(total_a_pagar / 3, 2)
    print(f'Total a pagar')