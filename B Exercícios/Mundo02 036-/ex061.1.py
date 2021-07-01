primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + 9 * razão
próximo = primeiro
if razão != 0:
    print('Os 10 primeiros termos da PA de {} com razão {} são: '.format(primeiro, razão),end='')
    while próximo != décimo + razão:
            próximo = próximo + razão
            print('{}'.format(próximo),end='')
            print('. ' if próximo == décimo + razão else ', ',end='')
else:
    print('A razão não pode ser 0')
