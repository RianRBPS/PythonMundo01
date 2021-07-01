n = 1
par = impar = 0
while n != 0: #FLAG (Condição de Parada)
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} número pares '
      'e {} números impáres!'.format(impar, par))


c = 1
while c < 10:
    c += 1
    print(c)
print('Fim')  #Sei ou não sei o limite

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')