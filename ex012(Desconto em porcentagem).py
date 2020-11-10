p1 = float(input('Preço do produto original: R$'))
p2 = p1 * 0.05
pf = p1 - p2
print('O produto que custava R${:.2f}, na promoção com 5% de desconto ficará: R${:.2f}'.format(p1, pf))
