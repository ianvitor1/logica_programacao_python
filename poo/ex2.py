class Produto:
    def __init__(self, codigo: str, nome: str, quantidade: str, preco: float):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

def impressao(produto):
    print(f'Código: {produto.codigo}')
    print(f'Produto: {produto.nome}')
    print(f'Quantidade: {produto.quantidade}')
    print(f'Preço: {round(produto.preco, 2)}') 

produtos = []
while True:
    codigo = input('Digite o código: ')
    nome = input('Digite o nome do produto: ')
    quant = int(input('Digite a quantidade: '))
    preco = float(input('Digite o preço: '))

    produto = Produto(codigo, nome, quant, preco)
    produtos.append(produto)

    sair = input('Digite S para sair ou Enter para continuar: ')
    if sair.upper() == 'S':
        break
print('\n ##### Lista de Produtos #####')
for produto in produtos:
    impressao(produto)
    print('')

print('##### Pesquisa de Produto #####')
busca = input('Digite o código do produto que deseja buscar: ')
achei = None
for produto in produtos:
    if busca == produto.codigo:
        achei = produto
        break
if achei is not None:
    impressao(achei)
else:
    print('Produto não encontrado!')