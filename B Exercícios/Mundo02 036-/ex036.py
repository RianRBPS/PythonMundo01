# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_da_casa = float(input('Digite o valor da casa: R$'))
salário = float(input('Digite o salário mensal do comprador: R$'))
anos_para_pagar = int(input('Quantos anos para pagar o empréstimo? '))
meses_para_pagar = (anos_para_pagar * 12)
prestação_mensal = valor_da_casa / meses_para_pagar
mínimo = salário * 0.3
print('Para comprar uma casa de R${}, com um salário de R${} em {} anos,'.format(valor_da_casa, salário, anos_para_pagar), end='')
print(' será necessário pagar mensalmente um valor de R${:.2f}.'.format(prestação_mensal, mínimo))
if prestação_mensal >= mínimo:
    print('Sendo assim, o empréstimo foi negado')
else:
    print('Sendo assim, o empréstimo foi aprovado')
