                     # Interactive Help
    # help (Python console)
    # help(print())
    # print(input.__doc__)

                        # docstrings
def contador(i, f, p):
    '''
    docstring
    Faz uma contagem e mostra na tela
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    '''
    c = i
    while c <= f:
        print(f'{c}',end='..')
        c += p
    print('FIM!')


              # Argumentos opcionais

def somar(a = 0, b = 0, c = 0):
    '''
    Faz a soma entre três valores na tela
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    '''
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(8, 4)   # O valor não informado vai valer 0
somar()       # Tudo vale 0

                  # Escopo de variáveis

def teste(b):
    global a # a vai valer 5
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5 # Programa principal
teste(a)
print(f'A fora vale {a}')

                     # Retorno de resultados

def somar(a = 0, b = 0, c = 0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}.     ')


