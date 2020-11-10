print('-=-'*10)
print('Calculadora de IMC')
print('-=-'*10)
c1 = float(input('Digite seu peso em kg: '))
c2 = float(input('Digite sua altura: '))
print('-=-'*10)
calc1 = c2*c2
calc2 = c1//calc1
print(calc2)
if calc2<18.5:
    print('Abaixo do peso')
elif calc2>18.5 and calc2<25:
    print('Peso ideal')
elif calc2>25 and calc2<=30:
    print('Sobrepeso')
elif calc2>30 and calc2<=40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
