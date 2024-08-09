def conceito(ma):
    if ma < 40:
        return 'E'
    elif ma < 60:
        return 'D'
    elif ma < 75:
        return 'C'
    elif ma < 90:
        return 'B'
    else:
        return 'A'
    
def resultados(conceito):
    if conceito == 'A' or conceito == 'B' or conceito == 'C':
        return 'APROVADO'
    else:
        return 'REPROVADO'

matricula = input('Digite a matrícula: ')
nota1 = float(input('Digite a nota1: '))
nota2 = float(input('Digite a nota2: '))
nota3 = float(input('Digite a nota3: '))
ME = float(input('Digite a média de exercicíos: '))
ma = (nota1 + nota2 * nota3 * 3 + ME) / 7
print('\n############# RESULTADOS #################')
print(f'Matrícula: {matricula}')
print(f'Nota 1: {nota1} | Nota 2: {nota2} | Nota 3: {nota3} | ME: {ME}')
print('Média de aproveitamento MA: {ma}')
print(f'Conceito: {conceito(ma)}')
print(f'Resultado: {resultados(conceito(ma))}')