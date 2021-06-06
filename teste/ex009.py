#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
'''
n = int(input('Digite um número:'))
a = 1*n
b = 2*n
c = 3*n
d = 4*n
e = 5*n
f = 6*n
g = 7*n
h = 8*n
i = 9*n
j = 10*n
print('A tabuada do {} é {}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(n, a, b, c, d, e, f, g, h, i, j))
'''

num = int(input('Digite um número para ver sua tabuada:'))
print('='*12)
print('{} x {:2} = {}'.format(num, 1, num*1))
print('{} x {:2} = {}'.format(num, 2, num*2))
print('{} x {:2} = {}'.format(num, 3, num*3))
print('{} x {:2} = {}'.format(num, 4, num*4))
print('{} x {:2} = {}'.format(num, 5, num*5))
print('{} x {:2} = {}'.format(num, 6, num*6))
print('{} x {:2} = {}'.format(num, 7, num*7))
print('{} x {:2} = {}'.format(num, 8, num*8))
print('{} x {:2} = {}'.format(num, 9, num*9))
print('{} x {:2} = {}'.format(num, 10, num*10))
print('='*12)

