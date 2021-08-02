numeros = int(input('Digite um número: ')), int(input('Digite mais um número: ')), int(input('Digite mais um número: ')), int(input('Digite mais um número: ')), int(input('Digite mais um número: '))

# Quantas vezes apareceu o valor 9
print(numeros.count(9))

# Em que posição foi digitado o primeiro 3
if 3 in numeros:
    print(numeros.index(3))
else:
    print('O valor 3 não foi digitado')

# Quais foram os números pares
print({n for n in numeros if n % 2 == 0})