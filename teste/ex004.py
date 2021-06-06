'''

Módulo antigo

n = input('Digite alguma coisa')
print('O tipo primitivo desse valor é', type(n))
print('Só tem espaços?', n.isspace())
print('É um número?', n.isnumeric())
print('É uma letra?', n.isalpha())
print('É alfanúmerico?', n.isalnum())
print('Está em maiúsculo?', n.isupper())
print('Está minúsculo?', n.islower())
print('Está capitalizada?', n.istitle())
'''
#Desafio extra (Python 3.7):

n = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(n)}')
print(f'Só tem espaços? {n.isspace()}')
print(f'É um número? {n.isnumeric()}')
print(f'É alfabético? {n.isalpha()}')
print(f'É alfanumérico? {n.isalnum()}')
print(f'Está em maiúsculas? {n.isupper()}')
print(f'Está em minúsculas? {n.islower()}')
print(f'Está capitalizado? {n.istitle()}')
