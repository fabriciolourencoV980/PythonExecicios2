"""
Crie um programa que tenha uma tupla com várias palavras, depois disso, você deve mostrar, para cada
palavra, quais são as suas vogais
"""

palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudante', 'praticar',
            'trabalhador', 'futuro','mercado','programador')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
