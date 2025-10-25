"""
Desafio 035 mostrnado o tipo de triangulo que será formado
"""

print('-=-'*10)
print('Analisando se  triangulo')
print('-=-'*10)

r1 = float(input('Digite o valor do primeiro segmento: '))
r2 = float(input('Digite o valor do segundo segmento: '))
r3 = float(input('Digite o valor do terceiro segmento: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print(f'Os segmentos acima [PODEM] formar um triangulo!')
    if r1 == r2 == r3:
        print('Formam um Triângulo Equilátero')
    elif r1 != r2 != r3 != r1:
        print('Formam um Triângulo Escaleno')
    else:
        print('Formam um Triângulo Isóceles')
else:
    print(f'Os segmentos acima [NÃO PODEM] formar um triangulo!]!')


