#Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
ano_atual = date.today().year
ano_nascimento = 0
total_maiores = 0
for c in range(1, 8):
    ano_nascimento = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    if (ano_atual - ano_nascimento) >= 18:
        total_maiores += 1
print('O número de pessoas MENORES de idade é de {}'.format(7 - total_maiores))
print('O número de pessoas MAIORES de idade é de {}'.format(total_maiores))
