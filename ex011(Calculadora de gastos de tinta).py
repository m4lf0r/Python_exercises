l1 = float(input('Digite a largura da parede em M:'))
a1 = float(input('Digite a altura da parede em M:'))
m1 = a1 * l1
print('Sua parede tem a dimensão de {}m x {}m e sua área é de {}m²'.format(l1, a1, m1))
tinta = m1 / 2
print('Para você pintar essa parede, você vai precisar {} litros de tinta'.format(tinta))
