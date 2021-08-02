zero_vinte = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
              'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
              'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze',
              'Dezesseis', 'Dezessete','Dezoito', 'Dezenove', 'Vinte')
número = 0
while True:
    número = int(input('Digite um número entre 0 e 20: '))
    if número in range(0, 21):
        break
    else:
        print('Tente novamente. Digite um número entre 0 e 20: ')
print(f'Você digitou o número: {zero_vinte[número]}')
