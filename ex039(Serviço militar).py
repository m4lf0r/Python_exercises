from datetime import date
from time import sleep
d1 = int(input('Digite o dia do seu nascimento: '))
d2 = int(input('Digite o mês do seu nascimento: '))
d3 = int(input('Digite o ano do seu nascimento: '))
calc = date.today().year - d3
if calc<18:
    print('Você ainda vai se alistar no serviço militar')
    calc2 = 18 - calc
    sleep(1.5)
    print('Falta {} ano(s) para você se alistar.'.format(calc2))
elif calc==18:
    print('Está na hora de se alistar')
elif calc>18:
    print('Já passou da hora de se alistar.')
    calc3 = calc - 18
    sleep(1.5)
    print('Você ultrapassou o prazo em {} Ano(s) para seu alistamento.'.format(calc3))

