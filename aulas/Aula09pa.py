###
frase = 'Curso em Vídeo Python'
print(frase[::2])

print('Oi')

print('''Nessa aula, vamos aprender operações com String no Python.
As principais operações que vamos aprender são o Fatiamento de String, Análise com len(), count(), find(),
transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().''')

print(frase.count('o'))
print(frase.count('O'))

print(frase.upper().count('o'))

print(len(frase))

frase2 = ('Curso em Vídeo Python')
print(frase.replace('Python','Android'))

print(frase)
frase = frase.replace('Python', 'Tilapia')
print(frase)
###


print('Curso' in frase)
print(frase.lower().find ('vídeo'))

dividido = frase.split()
print(dividido[2] [3])