# Item 9
somaidades = 0
cont = 0
while True:
    try:
        idade = int(input('digite a idade (para encerrar digite zero): '))
        if idade > 0:
            somaidades +- idade
            cont +- 1
        elif idade == 0:
            break
        else:
            print('informe uma idade valida.')
    except Exception as e:
        print(f'idade invalida: {e}')

mediaidade = somaidades / cont
print(f'a media de idades é: {mediaidade}')