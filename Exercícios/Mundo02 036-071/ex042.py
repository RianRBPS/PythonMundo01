#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes

s1 = int(input('Primeiro segmento: '))
s2 = int(input('Segundo segmento: '))
s3 = int(input('Terceiro segmento: '))
if (s1 + s2) > s3 and (s2 + s3) > s1 and (s3 + s1) > s2:
    print('Os ângulos podem formar um triângulo.',end='')
    if s1 == s2 == s3:
        print(' O triângulo é equilátero.')
    elif s1 == s3 and s1 != s2 or s2 == s3 and s2 != s1 or s1 == s2 and s1 != s3:
        print(' O triângulo é isósceles.')
    else:
        print(' O triângulo é escaleno.')
else:
    print('Os ângulos não podem formar um triângulo.')
