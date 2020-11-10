sal = float(input('Qual o salário do funcionário: R$'))
if sal>=1250.00:
    a1 = sal*0.1+sal
    print('O salário com o adicional fica em R${}'.format(a1))
else:
    a2 = sal*0.15+sal
    print('O salário com o adicional fica R${}'.format(a2))