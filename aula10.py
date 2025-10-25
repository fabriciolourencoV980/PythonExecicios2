
"""
nome = str(input('Digite seu nome: '))
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
print(f'Bom dia,', nome)
"""

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2) / 2
print(f'A sua média foi: {m:.2}')

if m >= 6.0:
    print('Sua média foi boa')
else:
    print('Sua média foi ruim!')