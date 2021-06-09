# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

#import random
from random import shuffle
aluno1 = str(input('First student name:' ))
aluno2 = str(input('Second student name: '))
aluno3 = str(input('Third student name: '))
aluno4 = str(input('Fourth student name: '))
lista = [aluno2, aluno4, aluno3, aluno1]
shuffle(lista)
print('The presentation order shall be: ')
print(lista)

