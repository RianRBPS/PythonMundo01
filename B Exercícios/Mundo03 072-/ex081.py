lista = []
digitados = 0
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    digitados += 1
    print('Valor adicionado')
    continuar = input('Deseja continuar? [S/N] ').strip().upper()
    while continuar not in 'SsNn':
        continuar = str(input('Resposta não válida! Quer continuar? [S/N] '))
    if continuar == 'N':
        break
    elif continuar == 'S':
        print('Continuando!')
lista.sort()
print(f'\nVocê digitou os valores {lista}')
print(f'Foram digitados {digitados} números')
lista.sort(reverse=True)
print(f'A forma decrescente dos valores é {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado na lista')
