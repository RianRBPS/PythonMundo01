from Exercícios.Mundo03ex.ex115.lib.interface import *
from time import sleep


while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoas', 'Sair do Sistema'])
    if resposta == 1:
        cabeçalho('Opção 1')
    elif resposta == 2:
        cabeçalho('Opção 2')
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1)