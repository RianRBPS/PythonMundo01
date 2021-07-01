n = int(input('Digite um número para ver seu Fatorial: '))
f = 1
c = 0
for c in range(1, n):
    f = f * n
    n = n - 1
print('Seu fatorial é {}'.format(f))
