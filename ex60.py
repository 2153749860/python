'''from math import factorial
num = int(input('Digite um número para calcular o seu fatorial: '))
fat = factorial(num)
print('O fatorial de {} é igual a {}.'.format(num, fat))'''



num = int(input('Digite um número para calcular o seu fatorial: '))
contador = num       # O contador começa pelo num
fatorial = 1
print('Calculando {}! = '.format(num), end='')
while contador > 0:
    print('{} '.format(contador), end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1
print('{}'.format(fatorial))
