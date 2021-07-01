from random import randint
cont = 0
while True:
    computador = randint(1, 2)
    print('-=' * 20)
    print('VAMOS JOGAR UMA PARTIDA')
    print('-=' * 20)
    jogador = int(input('Digite um número: '))
    print('-=' * 20)
    opção = str(input('Par ou Impar?'
                        '\n[ P ] Par'
                        '\n[ I ] Impar'
                        '\nOpção:')).strip().upper()[0]
    if opção == 'P':
        if (computador + jogador) % 2 == 0:
            print(f'Você ganhou! O computador jogou {computador}')
            cont += 1
        else:
            print(f'Você perdeu! O computador jogou {computador}')
            print(f'Você tinha ganhado {cont} vezes seguidas')
            break
    elif opção == 'I':
        if (computador + jogador) % 2 == 1:
            print(f'Você ganhou! O computador jogou {computador}')
            cont += 1
        else:
            print(f'Você perdeu! O computador jogou {computador}')
            print(f'Você tinha ganhado {cont} vezes seguidas')
            break
    else:
        print('Opção INVÁLIDA!')
