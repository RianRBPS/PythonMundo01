n = c = 0
while True:
    print('-=' * 21)
    n = int(input('Digite um número para ver sua tabuada: '))
    print('-=' * 21)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {c * n}')
print('Número negativo, programa encerrado')
print('-=' * 21)
