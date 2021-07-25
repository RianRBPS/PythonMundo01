lista = []
maior = menor = 0
for c in range(1, 6):
    n = int(input(f'Digite o valor da posição {c}: '))
    if c == 1:
        maior = n
    else:
        if n > maior:
            maior = n
    if c == 1:
        menor = n
    else:
        if n < menor:
            menor = n
    lista.append(n)
print(f'Você digotou os valores {lista}')
print(f'O maior valor digitado foi {maior} na posição ',end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')
print(f'\nO menor valor digitado foi {menor} na posição ',end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...',end='')