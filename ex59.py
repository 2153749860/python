primNum = int(input('Digite o primeiro valor: '))
segNum = int(input('Digite o segundo valor: '))
print('-=-'*15)
print('[1] somar'
      '[2] multiplicar'
      '[3] maior'
      '[4] novos valores'
      '[5] sair do programa')
opção = False
while opção == 1 or 2 or 3 or 4 or 5:
    opção = int(input('Digite a sua opção: '))
    if opção == 5:
        opção = True
    else:
        if opção == 1:
            soma = primNum + segNum
            print('A soma dos dois valores digitados é igual a {}'.format(soma))
        elif opção == 2:
            multiplicação = primNum * segNum
            print('O produto da multiplicação entre estes valores é igual a {}'.format(multiplicação))
        elif opção == 3:
            if primNum < segNum:
                print('O maior valor é {}'.format(segNum))
            if primNum > segNum:
                print('O maior valor é {}'.format(primNum))
        elif opção == 4:
            novoPrim = int(input('Digite um novo primeiro valor: '))
            novoPrim = primNum
            novoSeg = int(input('Digite um novo segundo valor: '))
            novoSeg = segNum
    
