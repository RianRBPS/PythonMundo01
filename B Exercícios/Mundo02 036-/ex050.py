p = 0
cont = 0
for c in range(0, 6):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        p = p + n
        cont = cont + 1
print('A soma de todos os valores pares é {} e o número de valores válido foi {}.'.format(p, cont))
