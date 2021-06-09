#Crie um programa que leia um número inteiro
# e mostre na tela se ele é PAR ou ÍMPAR.

import math
número = int(input('Digite um número: '))
if (número % 2) == 0:
    print('O número {} é Par'.format(número))
else:
    print('O número {} é Impar'.format(número))

#O resto da divisão de um número por n pode ser:
#0, 1, 2, 3, ..., (n-1)
