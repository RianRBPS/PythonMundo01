número = int(input('Digite um número inteiro: '))
count = 0
for c in range(1, número + 1):
    if número % c == 0:
        count = count + 1
        print('\033[32m',end=' ')
    else:
        print('\033[31m',end=' ')
    print('{} '.format(c),end=' ')
print('\n\033[mO número {} foi divísvel {} vezes.'.format(número, count))
if count == 2:
    print('\033[mNúmero primo.')
else:
    print('\033[mNão é número primo.')
