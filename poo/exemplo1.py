class Aluno:
    def __init__(self,matricula,nome,notas):
        self.matricula = matricula
        self.nome = nome
        self.notas = notas
        self.media = 0
        self.conceito = ''
        self.resultado = ''

    def conceito_aluno(self):
        if self.media >= 9:
            return 'A'
        elif self.media >= 7.5 and self.media < 9:
            return 'B'
        elif self.media >= 6 and self.media < 7.5:
            return 'C'
        elif self.media >= 4 and self.media < 6:
            return 'D'
        else: 
            return 'E'
        
    def resultado_aluno(self):
        if self.conceito == 'A' or self.conceito == 'B' or self.conceito == 'C':
            return 'Aprovado'
        else:
            return 'Reprovado'
        
def impressao(aluno):
    print(f'Matricula: {aluno.matricula}')
    print(f'Aluno: {aluno.nome}')
    print(f'Notas: {aluno.notas}')
    print(f'Média: {round(aluno.media, 1)}')
    print(f'Conceito: {aluno.conceito}')
    print(f'Resultado: {aluno.resultado}')

aluno1 = Aluno('810703', 'Ian', [8, 9, 10])
aluno1.media = sum(aluno1.notas) / len(aluno1.notas)
aluno1.conceito = aluno1.conceito_aluno()
aluno1.resultado = aluno1.resultado_aluno()

aluno2 = Aluno('810704', 'Felipe', [4, 5, 6])
aluno2.media = sum(aluno2.notas) / len(aluno2.notas)
aluno2.conceito = aluno2.conceito_aluno()
aluno2.resultado = aluno2.resultado_aluno()

impressao(aluno1)
print('')
impressao(aluno2)