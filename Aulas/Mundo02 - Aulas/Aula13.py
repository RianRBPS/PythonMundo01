
#for c in range(6, 0, -1): contar pra trás

#for c in range(0, 7, 2): pular casas (2 em 2 no caso)

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s = s + n
    # s += n
print('O somatório de todos é: {} '.format(s))



i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')


n = int(input('Digite um número: '))
for c in range (0, n+1):
    print(c)
print('Fim')