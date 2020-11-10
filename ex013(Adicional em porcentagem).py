salario = float(input('Qual é o salário do funcionário? R$'))
aumentop = salario * 0.15
aumentof = salario + aumentop
print('O funcionário ganhava R${:.2f},com o aumento salarial de 15% passa a receber:R${:.2f}'.format(salario, aumentof))