lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado')
    else:
        print('Valor já existente na lista!')
    continuar = input('Deseja continuar? [S/N] ').strip().upper()
    while continuar not in 'SsNn':
        cont = str(input('Resposta não válida! Quer continuar? [S/N] '))
    if continuar == 'N':
        break
    elif continuar == 'S':
        print('Continuando!')
lista.sort()
print(f'Você digitou os valores {lista}')

while cont not in 'SsNn':
    cont = str(input('Resposta não válida! Quer continuar? [S/N] '))
