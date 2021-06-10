#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
computador = randint(0,5) #Faz o computador escolher um número de 0 a 5
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar...')
print('-=-' * 20)

jogador = int(input('Em que número eu pensei? '))
print('Processado...')
sleep(2)
if jogador == computador:
    print('Parabéns, você acertou!')
else:
    print('Você errou!')
    print('Eu pensei no número {}'.format(computador))
