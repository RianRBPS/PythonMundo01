#O último valor não entra na contagem
frase = ('Curso em Vídeo Python')

importante = int(input('Número de 1 a 5: '))

if importante == 1:
    print(frase[9::3]) #VePh #A partir do 9 e pular de 3 em 3
    print(len(frase)) #21
    #Número de Caractéres

    print(frase.count('o')) #Quantas vezes aparece um 'o' minúsculo
    print(frase.count('o',0,13)) #(Fatiamente) Quantas vezes do 0 até o 12 aparece um 'o' minúsculo

    print(frase.find('deo')) #A partir de qual casa ele encontrou 'deo'
    print(frase.find('Android')) # -1 = A str não existe

    print('Curso' in frase) #True or False
elif importante == 2:
    print (frase[9:13]) #Vídeo

    print(frase[9:21]) #Vídeo Python

    print(frase[9:21:2]) #VdoPto #Saltar de 2 em 2

    print(frase[:5]) #Curso

    print(frase[15:]) #Python #Vai pegar do Python pra frente

    frase.replace('Python','Android')
    # ?
elif importante == 3:
    print(frase.upper()) #Todas as letras que eram minúsculas ficam maiúsculas
    print(frase.lower()) #Inverso do upper
    print(frase.capitalize())#Só a primeira letra vai ficar maiúscula
    print(frase.title()) #Todas as primeiras letras vão ficar maiúsculas
    print(frase.strip()) #Remove todos os espaços inúteis
    print(frase.rstrip()) #Remove todos os espaços inúteis da direita
    print(frase.lstrip()) #Remove todos os espaços inúteis da esquerda
elif importante == 4:
    print(frase.split())
    #Divide todas as palavras em uma lista
    #['Curso', 'em', 'Vídeo', 'Python']

    frase2 = ['Curso', 'em', 'Vídeo', 'Python']
    print('-'.join(frase2))
    #Junta tudo e separa pelo '-'
else:
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
    print(frase.replace('Python', 'Android'))

    print(frase)
    frase = frase.replace('Python', 'Tilapia')
    print(frase)
    ###

    print('Curso' in frase)
    print(frase.lower().find('vídeo'))

    dividido = frase.split()
    print(dividido[2][3])
