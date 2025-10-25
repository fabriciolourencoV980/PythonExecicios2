"""
Leia o ano de nascimento de um jovem e informe, de acordo com a idade
se ele ainda vai se alistar no quartel
se é hora de se alistar
se já passou do tempo de se alistar
O programa deve mostrar o tempo que falta ou se o prazo já passou
"""

from datetime import date

anoNascimento =  int(input('Digite seu ano de nascimento: '))
sexo = str(input('Digite seu sexo (M/F): ')).upper()
data = date.today()
anoAtual = data.year
alistamento = anoAtual - anoNascimento
print(f'Quem nasceu em {anoNascimento} tem {anoAtual - anoNascimento} anos em {anoAtual}.')

if sexo == 'M':
    if alistamento < 18:
        print(f'Você ainda vai se alistar no serviço militar, falta exatamente {18 - alistamento} anos.')
    elif alistamento == 18:
        print(f'Já está na hora de se alistar no serviço militar!')
    elif alistamento > 18:
        print(f'Já passou da hora de se alistar! Você ultrapassou {alistamento - 18} anos do prazo militar!.')
else:
    print('[O ALISTAMENTO NÃO É OBRIGATÓRIO]')