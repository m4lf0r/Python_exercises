from datetime import date
ano = int(input('Digite o ano de seu nascimento: '))
calc= date.today().year-ano
print(calc)
if calc<=9:
    print('Categoria: MIRIM')
elif calc>=10 and calc<=14:
    print('Categoria: INFANTIL')
elif calc>=15 and calc<=19:
    print('Categoria: JUNIOR')
elif calc==20:
    print('Categoria: SÊNIOR')
elif calc>20:
    print('Categoria: MASTER')
