def lin():
    print('*' * 30)


# Program principal (Duas linhas entre o def e ele por estética)
lin()
print('  Curso em Vídeo  ')
lin()
print('  APRENDA PYTHON   ')
lin()
print('  GUSTAVO GUANABARA   ')
lin()


def mensagem(msg):
    print('+++++++++++++++++++')
    print(msg)
    print('+++++++++++++++++++')


mensagem('SISTEMA DE ALUNOS')


def título(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)

#Programa principal
título('  CURSO EM VÍDEO   ')
título(' APRENDA PYTHON ')


def soma(a, b):
    s = a + b
    print(s)


soma(4, 5)
soma(8, 9)
soma(2, 1)


def contador(*núm): #Empacotamento
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números!')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


def dobra(lst):
    pos = 0
    while pos < len(lst):  
        lst[pos] += 2
        pos += 1


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)