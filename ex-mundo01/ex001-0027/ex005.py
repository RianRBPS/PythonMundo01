#Faça um programa que leia um número inteiro e moste na tela o seu sucessor e seu antecessor

'''
n = int(input('Digite um número: '))
na = n + 1
nb = n - 1
print('O antecessor de {} é {} e o seu sucessor é {}'.format(n, nb, na))
'''

n = int(input('Digite um número: '))
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1)))
