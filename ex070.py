"""
crie um programa que leia o nome e o preço do produto. O programa vai perguntar
se o usuário deseja continuar. No final, mostre:
a qual é o total gasto da compra
b quantos produtos custam mais 1000
c qual o nome do produto mais barato
"""

cont = total = menor = cont1 = 0
barato = ''

while True:
    print('-=' * 10)
    print('LOJA SUPER BARATÃO')
    print('-=' * 10)
    nome = str(input('Nome do produto: '))
    valor = float(input('Preço: R$'))
    cont1 += 1
    total += valor
    if valor > 1000:
        cont += 1
    if cont1 == 1 or valor < menor:
        menor = valor
        barato = nome
    opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        print('=' * 8, 'FIM DO PROGRAMA', '=' * 8)
        break

print(f'O total da compra foi de R${total}')
print(f'Temos {cont} produtos custando mais de R$1000')
print(f'O produto mais barato foi: {barato} que custa R${menor} ')