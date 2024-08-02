altura = float(input('Digite a altura:'))
sexo = input('Digite o sexo: ')
peso = float(input('Digite o peso:'))

pesoIdeal = 0.0
if(sexo.upper() == 'M'): #Lower
    pesoIdeal = (72.7*altura)-58

elif(sexo.upper() == 'F'):
    pesoIdeal = (62.1*altura)-44.7
else:
    print('O sexo informado deve ser M para Masculino ou F para Feminino.')

if(pesoIdeal > 0):
    print('O sexo informado  foi: ', sexo.upper())
    print('Seu peso ideal é: ', round(pesoIdeal, 2))

IMC = round(peso/altura**2 ,1)

if IMC < 18.5:
    print('Abaixo do peso')
elif IMC < 25:
    print('Peso Normal')
elif IMC < 30:
    print('Sobrepeso')
elif IMC < 35:
    print('Obesidade grau 1')
elif IMC < 40:
    print('Obesidade grau 2')
else:
    print('Obesidade grau 3')
