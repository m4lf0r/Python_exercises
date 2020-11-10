n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
calc = n1+n2//2
if calc<5.0:
    print('REPROVADO!')
elif calc>=5.0 or calc<=6.9:
    print('RECUPERAÇÃO!')
elif calc>=7.0:
    print('APROVADO!')