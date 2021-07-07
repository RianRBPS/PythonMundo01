numeros = int(input('Digite um número: ')), int(input('Digite mais um número: ')), int(input('Digite mais um número: ')), int(input('Digite mais um número: ')), int(input('Digite mais um número: '))

# Quantas vezes apareceu o valor 9
print(numeros.count(9))

# Em que posição foi digitado o primeiro 3
print(numeros.index(3))

# Quais foram os números pares
print({n for n in numeros if n % 2 == 0})