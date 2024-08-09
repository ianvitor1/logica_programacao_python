preco = float(input('Preço do produto: '))
print('1- A vista em dinheiro ou cheque' )
print('2- A vista no cartao de credito' )
print('3- Em duas vezes no cartão de crédito')
print('4- Em tres vezes no cartão de crédito, juros de 10%')

condicao = int(input('Código Condição de pagamento: '))

if condicao == 1:
    total = preco - 10/100 * preco 
    print(f'Total a pagar com 10% de desconto: {total}')
elif condicao == 2:
    total = preco - 15/100 * preco 
    print(f'Total a pagar com 15% de desconto: {total}')
elif condicao == 3:
    total = round(preco / 2, 2)
    print(f'Total a pagar 2x de: {total}')
elif condicao == 4:
    total = preco + 10/100 * preco 
    total = round