primNum = int(input('Digite o primeiro valor: '))
segNum = int(input('Digite o segundo valor: '))
opção = 0
while opção != 5:
    print('''[1] somar
[2] multiplicar
[3] maior
[4] novos valores
[5] sair do programa''')
    opção = int(input('Digite a sua opção: '))
    if opção == 1:
        soma = primNum + segNum
        print('A soma dos dois valores digitados é igual a {}'.format(soma))
    elif opção == 2:
        multiplicação = primNum * segNum
        print('O produto da multiplicação entre os dois valores é igual a {}'.format(multiplicação))
    elif opção == 3:
        if primNum < segNum:
            print('O maior valor é {}'.format(segNum))
        if primNum > segNum:
            print('O maior valor é {}'.format(primNum))
    elif opção == 4:
        print('Digite os novos valores.')
        primNum = int(input('Digite um novo primeiro valor: '))
        segNum = int(input('Digite um novo segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Digite novamente: ')
print('Fim do programa!')
    
