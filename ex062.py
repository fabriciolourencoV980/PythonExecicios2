"""
Melhore o desafio 061
"""

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('FIM')
    print('-=' * 10)
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')
print('-=' * 10)
print(f'Progressão finalizada com {total} termos mostrados.')