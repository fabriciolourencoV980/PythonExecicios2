"""
Crie uma Tupla preenchida com os 20 primeiros colocados da tabela do campeonato Brasileiro de futebol,
na ordem da colocação. depois mostre:
A) Apenas os 5 primeiros colocados da tabela do campeonato
B) Os 4 últimos colocados da tabela do campeonato
C) Uma lista de times em ordem alfabetica
D) Mostrar o time que está em Oitava posição
"""


times = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Mirassol', 'Botafogo', 'Bahia', 'Fluminense', 'São Paulo',
         'Vasco da gama', 'Bragantino', 'Grêmio', 'Corintians', 'Ceará SC', 'Internacional', 'Internacional',
         'Atlético-MG', 'Santos', 'Ec Vitória', 'Fortaleza', 'Juventude', 'Sport Recife')

print('-=' * 22)
print('Todos os 20 times do Brasileirão Seerie A')
print('-=' * 22)

for indice, num in enumerate(times, start=1):
    print(indice, num)

print('-=' * 22)
print('Os 5 primeiros colocados da tabela do campeonato')
print('-=' * 22)

for indice, n in enumerate(range(0, len(times[:5])), start=1):
    print(indice, times[n])

print('-=' * 22)
print('Os 4 últimos colocados da tabela do campeonato')
print('-=' * 22)

for num, time in enumerate(times[17:], start= 17):
   print(num, time)

print('-=' * 22)
print('Lista com os times em ordem alfabetica')
print('-=' * 22)

for time in sorted(times):
    print(time)

print('-=' * 22)
for indice, time in enumerate(times, start=1):
    if indice == 8:
        print(f'O time {time} está em 8ª Posição')