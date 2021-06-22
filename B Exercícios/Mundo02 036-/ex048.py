s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        s = s + c
print('A soma de todos os valores solicitados é {} e'.format(s),end='')
print(' a quantidade de valores é {}.'.format(cont))
