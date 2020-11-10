from time import sleep
print('-=-'*15)
print('         ANALISADOR DE TRIÂNGULOS')
print('-=-'*15)
l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))
sleep(1.5)
print('-=-'*20)
if l1<=l2+l3 and l2<=l1+l3 and l3<=l1+l2:
    print('Os segmentos acima são possíveis formar um TRIÂNGULO!')
else:
    print('Os segmentos acima não formam um TRIÂNGULO!')
print('-=-'*20)