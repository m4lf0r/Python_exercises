nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome completo em maiusculo: {}'.format(nome.upper()))
print('Seu nome completo em minusculo: {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome)-nome.count(' ')))
#print('seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split() #dividir por string sem espaços
print(separa)
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))