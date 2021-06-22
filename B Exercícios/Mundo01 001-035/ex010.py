#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
n = float(input('Quanto você tem na carteira em reais? R$'))
d = n/5.212
print('Com os seus R${:.2f} você poderia comprar {:.2f} dólares no dia 30 de março de 2021'.format(n, d))
