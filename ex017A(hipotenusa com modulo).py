from math import hypot
co = float(input('Qual o comprimento do cateto oposto: '))
ca = float(input('Qual o comprimento do cateto adjacente:'))
hi = hypot(co, ca)
print('A hipotenusa vai medir: {:.2f}'.format(hi))
# Uso da biblioteca math