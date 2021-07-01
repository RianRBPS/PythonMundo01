#Mais eficiente
print('Os números pares no intervalo de 1 a 50 são:')
for c in range(2, 51, 2):
    print(c, end=' ')
print('Fim')

for n in range(1, 51):
    if n % 2 == 0:
        print(n, end=' ')
print('Fim')