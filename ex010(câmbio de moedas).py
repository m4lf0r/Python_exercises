real = float(input('Quanto em dinheiro você tem na carteira? R$'))
dolar = real / 5.31
euro = real / 5.77
bitcoin = real / 36708.45
print('Com R${:.2f} você pode comprar U$${:.2f}'.format(real, dolar))
print('Com R${:.2f} você pode comprar €$${:.2f}'.format(real, euro))
print('Com R%{:.2f} você pode comprar ₿TC${:.5f}'.format(real, bitcoin))
