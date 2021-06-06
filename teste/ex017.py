# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

'''
co = float(input('Qual o comprimento do cateto oposto?'))
ca = float(input('Qual o comprimento do cateto adjacente?'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('Cateto oposto: {}\nCateto adjacente: {}\nHipotenusa: {:.3f}\n'.format(co, ca, hi))
'''

import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.3f})'.format(hi))

# from math import hypot


