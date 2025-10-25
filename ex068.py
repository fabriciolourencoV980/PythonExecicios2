"""
Faça um programa que jogue par ou impar com o computador. O jogo será interrompido quando o
jogador perder, mostrando o total de vitorias consecutivas que ele conquistou no final
"""

from random import randint

cont = 0

while True:
    computador = randint(1, 10)
    valor = int(input('Digite um valor: '))
    escolha = str(input('Par ou impar? [P/I]: ').upper().strip()[0])
    total = computador + valor
    if escolha == 'P':
        print('~~' * 30)
        print(f'Você jogou {valor} e o computador {computador}. Total de {valor + computador} DEU PAR.')
        print('~~' * 30)
        if total % 2 == 0:
            cont += 1
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
        else:
            print('Você PERDEU!')
            break
    elif escolha == 'I':
        print('~~' * 30)
        print(f'Você jogou {valor} e o computador {computador}. Total de {valor + computador} DEU IMPAR.')
        print('~~' * 30)
        if total % 2 == 1:
            cont += 1
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
        else:
            print('Você PERDEU!')
            break
print('-=' * 30)
print(f'GAME OVER! Você venceu {cont} vezes.')

