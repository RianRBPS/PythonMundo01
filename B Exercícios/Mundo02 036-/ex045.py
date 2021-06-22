# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
jogador = int(input('''Suas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL 
[ 2 ] TESOURA
Qual é a sua escolha? '''))
if jogador == 0 or jogador == 1 or jogador == 2:
    print('-=' * 11)
    sleep(1)
    print('JO!')
    sleep(1)
    print('KEN!')
    sleep(1)
    print('PO!')
    print('Computador jogou {}'.format(itens[computador]))
    print('Jogador jogou {}'.format(itens[jogador]))
    print('-=' * 11)
    if computador == 0: #computador jogou PEDRA
        if jogador == 0:
            print('Empate!')
        elif jogador == 1:
            print('Jogador ganhou!')
        elif jogador == 2:
            print('Jogador perdeu')
        else:
            print('Jogada Inválida')
    elif computador == 1: #computador jogou PAPEL
        if jogador == 0:
            print('Jogador perdeu!')
        elif jogador == 1:
            print('Empate!')
        elif jogador == 2:
            print('Jogador ganhou!')
        else:
            print('Jogada Inválida')
    elif computador == 2: #computador jogou TESOURA
        if jogador == 0:
            print('Jogador ganhou!')
        elif jogador == 1:
            print('Jogador perdeu!')
        elif jogador == 2:
            print('Empate!')
        else:
            print('Jogada Inválida')
else:
    print('Opção Inválida!')
