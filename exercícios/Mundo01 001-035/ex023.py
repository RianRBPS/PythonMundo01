#Faça um programa que leia um número de 0 a 9999
# e mostre na tela cada um dos dígitos separados

number = int(input('Informe um número: '))
u = (number // 1) % 10
# u = (number) % 10
d = (number // 10) % 10
c = (number // 100) % 10
m = (number // 1000) % 1000
print('Analisando o número {}'.format(number))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centana: {}'.format(c))
print('Milhar: {}'.format(m))
