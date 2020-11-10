vel = float(input('Qual a velocidade do carro? '))
if vel >80:
    print('MULTADO! Você excedeu o limite de velocidade permitido que é 80Km/h')
    multa = (vel-80)*7
    print('Você deve pagar uma multa no valor de R${:.2f}'.format(multa))
    print('Dirija com cuidado!')
print('Tenha um bom dia, dirija em segurança')