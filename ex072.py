"""
Crie um programa que tenha uma tupla totoalmente preenchida com uma contagem de por extenso de 0 até 20

Seu programa deverá ler um número pelo techado (entre 0 e 20) e mostrá-lo por extenso
"""

numero = int(input('Digite um número entre 0 e 20: '))
extenso = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove','Dez', 'Onze', 'Doze',
           'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')

for indice, num in enumerate(extenso):
    indicador = indice
    if numero == indicador:
        print(f'O número digitado foi {num}')