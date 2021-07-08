vogais = ('a', 'e', 'i', 'o', 'u')
palavras = ('Viajar', 'Elegante', 'Animal', 'Carro', 'Brasileiro', 'Abacate')

for p in palavras:
    print(f'\nNa palavra {p} temos ',end='')
    for letra in p:
        if letra in vogais:
            print(letra,end=' ')