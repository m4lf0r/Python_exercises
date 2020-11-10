numero = int(input('Digite um número para saber se é par ou impar: '))
resto = numero%2
if resto ==0:
    print('O número {} é par!'.format(resto))
else:
    print('O número {} é impar!'.format(resto))
