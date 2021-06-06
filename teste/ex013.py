#Faça um algoritmo que leia um salário de um funcionário e mostre seu novo salário, com 15% de aumento
s = float(input('Qual é o salário atual do funcionário? R$'))
a = s*1.15
print('O salário do funcionário atual de R${:.2f} vai passar a ser R${:.2f} após o aumento de 15%'.format(s, a))

# a = a + (s * 15 / 100)
