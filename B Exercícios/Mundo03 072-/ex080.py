lista = []
for c in range(1, 6):
    n = int(input(f'Digite o {c} valor: '))
    if c == 1 or n > lista [-1]:
        lista.append(n)
    #elif n > lista[len(lista) - 1]:
    #elif n >lista[-1]:
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')