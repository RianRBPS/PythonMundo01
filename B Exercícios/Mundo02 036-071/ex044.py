#: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros

print('{:=^40}'.format(' LOJA '))
preço = float(input('Digite o preço da compra: R$'))
print('''Formas de Pagamento
[ 1 ] à vista dinheiro ou cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Sua opção: '))
if opção == 1:
    total = preço * 0.9
elif opção == 2:
    total = preço * 0.95
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.'.format(parcela))
elif opção == 4:
    total = preço * 1.20
    total_de_parcelas = int(input('Em quantas parcelas de seja pagar? '))
    parcelado = total / total_de_parcelas
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(total_de_parcelas, parcelado))
else:
    total = preço
    print('Opção de pagamento INVÁLIDA!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))



