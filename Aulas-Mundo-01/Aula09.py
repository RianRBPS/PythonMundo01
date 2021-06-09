frase = ('Curso em Vídeo Python')
print (frase[9:13])

#O último valor não entra na contagem
print(frase[9:21])

print(frase[9:21:2])
#Vai saltar de dois em dois
#VdoPto

print(frase[:5])
#Vai começar no início

print(frase[15:])
#Vai ir até o final, mesmo recurso do :21

print(frase[9::3])
#A partir do 9 e pular de 3 em 3
#VePh

print(len(frase))
#Número de Caractéres

print(frase.count('o'))
#Quantas vezes aparece um 'o' minúsculo

print(frase.count('o',0,13))
#(Fatiamente) Quantas vezes do 0 até o 12 aparece um 'o' minúsculo

print(frase.find('deo'))
#A partir de qual casa ele encontrou 'deo'

print(frase.find('Android'))
# -1 = A str não existe

print('Curso' in frase)
#True or False

frase.replace('Python','Android')
# ?

print(frase.upper())
#Todas as letras que eram minúsculas ficam maiúsculas

print(frase.lower())
#Inverso do upper

print(frase.capitalize())
#Só a primeira letra vai ficar maiúscula

print(frase.title())
#Todas as primeiras letras vão ficar maiúsculas
