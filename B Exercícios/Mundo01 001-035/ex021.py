#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

'''
import pygame
pygame.init()
pygame.mixer.music.load('T1scream.mp3')
pygame.mixer.music.play
pygame.event.wait()
'''
#O do Curso não funcionou, tive que ir atrás de uma outra forma de resolver

import pygame
pygame.mixer.init()
pygame.mixer.music.load('T1scream.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()): pass
