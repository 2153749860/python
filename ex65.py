'''contagem = 0
soma = 0
num = 0
média = 0
num = int(input('Digite um valor: '))
resposta = str(input('Pretende continuar? [S/N] ')).strip().upper()
if resposta == 'S':
    while resposta == 'S':
        num = int(input('Digite um valor: '))
        resposta = str(input('Pretende continuar? [S/N] ')).strip().upper()
        soma += num
        contagem += 1
elif resposta == 'N':
    print('FIM!')
média = soma / contagem
print('A média entre todos os valores digitados é igual a {}.'.format(média))'''






resposta = 'S'
média = soma = quantidade = maior = menor = 0
while resposta in 'Ss':
    número = int(input('Digite um valor: '))
    soma += número
    quantidade += 1
    if quantidade == 1:
        maior = menor = número
    else:
        if número > maior:
            maior = número
        elif número < menor:
            menor = número
    resposta = str(input('Pretende continuar? [S/N] ')).strip().upper()[0]
média = soma / quantidade
print('Você digitou {} números e a média entre eles é igual a {}.'.format(quantidade, média))
print('O maior número digitado é o {} e o menor é o {}.'.format(maior, menor))


