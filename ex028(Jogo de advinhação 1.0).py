from random import randint
from time import sleep
comp = randint(0,5) #Pensando um número aleatório.
print('-=-'*10)
print('Rodarei um número de 0 a 5...')
print('-=-'*10)
print(comp) #Fila contra a máquina
jogador = int(input('Qual seria o número correto? '))
print('Rodando os dados...')
sleep(3)
if jogador==comp:
    print('-'*35)
    print('PARBÉNS você ganhou!')
    print('-' * 35)
    sleep(2)
    print('Você ganhou exatamente nada !!!!!')
else:
    print('-=-'*20)
    print('Hahaha caiu no número {}, você errou!!'.format(comp))
    print('-=-'*20)
