class Produto:
    def __init__(self, codigo: str, nome: str, quantidade: str, preco: float):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

def desconto(self, percentual):
    return self.preco - self.preco * percentual / 100

def reajuste(self, percentual: float):
    return self.preco + self.preco * percentual / 100

def impressao(produto):
    print(f'Código: {produto.codigo}')
    print(f'Produto: {produto.nome}')
    print(f'Quantidade: {produto.quantidade}')
    print(f'Preço: {round(produto.preco, 2)}')

def cadastro():
    codigo = input('Digite o código: ')
    nome = input('Digite o nome do produto: ')
    quant = int(input('Digite a quantidade: '))
    preco = float(input('Digite o preço: '))

    produto = Produto(codigo, nome, quant, preco)

    return produto

def pesquisa():
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

def lista_produtos(produtos):
    print('\n ##### Lista de Produtos #####')
    for produto in produtos:
        impressao(produto)
        print('')  

produtos = []
while True:
    opcao = int(input('Escolha a opção desejada \n'
                  '1- Para cadastar produto'
                  '\n2- Para pesquisar produto'
                  '\n3- Para impressão da lista deprotutos'
                  '\n4- Para venda do produto'
                  '\n5- Para reajuste'

                  ))   
    if opcao == 1:
        produtos.append(cadastro())
    elif opcao == 2:
        pesquisa(produtos)
    

    sair = input('Digite S para sair ou Enter para continuar: ')
    if sair.upper() == 'S':
        break

print('##### Venda de Produto #####')
busca = input('Digite o código do produto: ')
perc = float(input('Digite o percentual do desconto:'))
achei = None
valor_desconto = 0.0
for produto in produtos:
    if busca == produto.codigo:
        achei = produto
        valor_desconto = produto.desconto(perc)
        produto.preco = valor_desconto
        break
if achei is not None:
    impressao(achei)
else:
    print('Produto não encontrado!')