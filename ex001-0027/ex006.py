#Crie um algoritmo que leia um número e mostre o seu dobro, tripo e raiz quadrada
'''
n = int(input('Digite um número:'))
na = n*2
nb = n*3
nc = n ** (1/2)
print('O dobro do número {} é {}, o tripo é {} e a raiz quadrada vale {}'.format(n, na, nb, nc))
'''

n = int(input('Digite um número: '))
#print('O dobro do número {} vale {}.\nO tripo vale {}.\nE a raiz quadrada vale {:.2f}.'.format(n, (n*2), (n*3), (n**(1/2))))
print('O dobro do número {} vale {}.\nO tripo vale {}.\nE a raiz quadrada vale {:.2f}.'.format(n, (n*2), (n*3), pow(n, (1/2))))

