'''
Faça um programa que leia a altura e largura de uma parede em metros, calcule a
sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro
de tinta pinta um área de 2m^2
'''

at = float(input('Qual é a altura da parede?'))
l = float(input('E qual é a largura da parede?'))
ar = at*l
t = ar/2
print('A área da parede {}x{} corresponde a {} metros quadrados.\nA quantidade de tinta para pintá-la é igual à {:.2f} litros'.format(at, l, ar, t))

