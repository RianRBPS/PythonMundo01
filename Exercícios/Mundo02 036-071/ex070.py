total_gasto = mais_d1000 = mais_barato  = cont = 0
barato = ''
while True:
    print('=-' * 20)
    nome = input('Nome do produto: ')
    preço = float(input('Preço do produto: R$'))
    cont += 1
    total_gasto += preço
    if preço > 1000:
        mais_d1000 += 1
    if cont == 1 or preço < mais_barato:
        mais_barato = preço
        barato = nome
    #else:
        #if preço < mais_barato:
            #mais_barato = preço
            #barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total_gasto:.2f}')
print(f'Temos {mais_d1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} custa R${mais_barato}')
