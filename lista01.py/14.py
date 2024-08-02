# Item 14
'''
ax2 + bx + c

delta = b2 -4c

raiz1 = (-b + raizquadrada(delta)) / 2a

raiz2 = (-b - raizquadrada(delta)) / 2a
'''

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))

delta = b*b -4*a*c #b**2

if delta < 0:
    print(f'delta {delta} - não a raizes')
if delta == 0:
    print(f'delta: {delta} - não é equação de segundo grau')
else:
    raiz1 = (-b + (delta**0.5)) / 2*a

    raiz2 = (-b - (delta**0.5)) / 2*a

print(f'delta: {delta} - raiz 1: {raiz1}, raiz 2: {raiz2}')