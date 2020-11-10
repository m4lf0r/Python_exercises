preco = float(input('Preço do produto: R$'))
print('-=-'*20)
print('Condiçoes de pagamento:1= Dinheiro/Cheque | 2=Cartão')
cond = int(input('Condição de pagamento: '))
print('-=-'*20)
print('À vista no dinheiro ou cheque=10% de desconto')
print('A vista no cartão= 5% de desconto')
print('Em até 2x no cartão= sem juros')
print('Em 3x ou mais= 20% de juros')
parc = int(input('Quantidade de parcelas: '))
print('-=-'*20)
if cond==1 and parc==1:
    calcp = preco*0.1
    calc1 = preco-calcp
    print('com 10% de desconto você irá pagar R${:.2f} no produto.'.format(calc1))
elif cond==2 and parc==1:
    calcz = preco*0.05-preco
    calc2 = preco-calcz
    print('Com 5$ de desconto você irá pagar R${:.2f} no produto.'.format(calc2))
elif cond==2 and parc==2:
    print('Você irá pagar R${:.2f} Parcelado em {}x '.format(preco, parc))
else:
    calc3=preco*0.2+preco
    print('Você irá pagar R${:.2f} parcelado em {}x'.format(calc3, parc))
