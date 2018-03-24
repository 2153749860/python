primeiro = int(input('Digite o primeiro termo da progressão: '))
razão = int(input('Digite a razão da progressão: '))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} '.format(termo), end='-> ')
        termo += razão
        contador += 1
    print('PAUSA!')
    mais = int(input('Quantos termos quer ver a mais? '))
print('Progressão finalizada com {} termos.'.format(total))
