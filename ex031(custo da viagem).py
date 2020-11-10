from time import sleep
dist = float(input('Qual a distância da sua viagem em Km: '))
print('Calculando o preço..')
sleep(2)
if dist <=200:
    preco = dist * 0.5
    print('Você irá pagar R${:.2f} para essa viagem'.format(preco))
else:
    preco = dist * 0.45
    print('Você irá pagar R${:.2f} para esta viagem'.format(preco))