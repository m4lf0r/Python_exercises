from math import radians, sin, cos, tan
an = float(input('Digite o angulo que você deseja: '))
sn = sin(radians(an))
co = cos(radians(an))
ta = tan(radians(an))
print('O ângulo {} tem o SENO de {:.2f}'.format(an, sn))
print('O ângulo {} tem o COSSENO de {:.2f}'.format(an, co))
print('O ângulo {} tem o TANGENTE de {:.2f}'.format(an, ta))


