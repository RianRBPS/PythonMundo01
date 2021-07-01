from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    palpites += 1
    jogador = int(input('Qual é seu palpite? '))
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('Menos... Tente novamente')
        elif jogador < computador:
            print('Mais... Tente novamente')
print('Acertou!')