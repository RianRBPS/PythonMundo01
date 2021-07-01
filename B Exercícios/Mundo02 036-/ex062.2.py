resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < maior:
            menor = núm
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0] #Considerar apenas a primeira letra
média = soma / quant
print('Você digitou {} números, a média entre eles é de {:.1f}'.format(quant, média))
print('O maior número foi {} e o menor foi {}'.format(maior, menor))
