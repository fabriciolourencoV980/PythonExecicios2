
resp = 'S'
media = quant = soma = maior = menor =0

while resp in 'Ss':
    num = int(input('Digite um número: '))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / quant
print('-=' * 10)
print(f'Você digitou {quant} números e a média foi {media:.1f}')
print(f'O maior número foi {maior} o menor foi {menor}')