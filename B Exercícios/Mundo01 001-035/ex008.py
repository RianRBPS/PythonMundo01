#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
v = float(input('Digite um valor em metros:'))
c = v*100
m = v*1000
print('O valor {} em centímetros vale {} e em milímetros vale {}'.format(v, c, m))
