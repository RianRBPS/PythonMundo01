print('SISTEMA DE AJUDA PyHELP')
print('-='*30)
while True:
    resp = input('\033[0;31mFunção ou Biblioteca >\033[m')
    if resp.upper() == 'FIM':
        print('\033[0;31mAté Logo!\033[m')
        break
    print(help(resp))