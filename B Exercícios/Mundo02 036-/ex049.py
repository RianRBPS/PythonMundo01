número = int(input('Digite um número para ver sua tabuada: '))
print('-=' * 11)
for contagem in range(1, 11):
    print('{} x {:2} = {}'.format(número, contagem, número * contagem))
print('-=' * 11)

