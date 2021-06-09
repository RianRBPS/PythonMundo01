#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

#import random
from random import choice
aluno1 = str(input('First student: '))
aluno2 = str(input('Second student: '))
aluno3 = str(input('Third student: '))
aluno4 = str(input('Fourth student: '))
lista = [aluno4, aluno3, aluno2, aluno1]
escolhido = choice(lista)
print('The selected student was {}'.format(escolhido))
