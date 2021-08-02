tentativas = 0
import pygame
from random import  randint
computador = randint(0, 10)

print('-=-' * 20)
print('Pensei em um número entre 0 e 10, tente adivinhar...')
print('-=-' *  20)
jogador = int(input('Em que número eu pensei? '))

while jogador != computador:
    tentativas += 1
    if jogador > computador:
        print('Menos... Tente novamente')
    elif jogador < computador:
        print('Mais... Tente novamente')
    jogador = int(input('Em que número eu pensei? '))
print('Você acertou! O número era {}!'
      '\nVocê precisou de {} tentativas!'.format(computador, tentativas))

pygame.mixer.init()
pygame.mixer.music.load('Fogos.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()): pass
