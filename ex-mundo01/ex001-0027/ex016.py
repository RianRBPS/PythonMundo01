#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porça inteira
#ex 6.127 tem a parte inteira 6

#math.trunc = corta a parte inteira

'''
Não funciona em números com mais de dois algorítmos inteiros
n = float(input('Digite um número real: '))
print('O número {} tem a parte inteira {:.0f}.'.format(n, n))
'''

'''
import math
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, math.trunc(num)))
'''

'''
from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, trunc(num)))
'''

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, int(num)))
