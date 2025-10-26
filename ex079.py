"""
Crie um programa onde o usuário possa digitar vários valores númericos e cadastra-se em uma lista.
Caso o número exista nela não será adicionado, no final será exibido todos os valores únicos
digitados em ordem crescente
"""
valores = list()

while True:
    num = int(input('Digite um valor: '))
    if num in valores:
        valores.pop()
        print('Valor Duplicado! Não será adicionado')
    else:
        valores.append(num)
        print('Valor adicionado com sucesso!')

    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'Ss':
        continue
    elif continuar in 'Nn':
        break
    if continuar not in 'NnSs':
        print('Digite um valor valido! [S/N] ')
        continuar1 = str(input('Deseja continuar?[S/N] '))
        while continuar1 not in 'SsNn':
            print('Digite um valor valido! [S/N] ')
            continuar1 = str(input('Deseja continuar?[S/N] '))
        if continuar1 in 'Ss':
            continue
        if continuar1 in 'Nn':
            break

crescent = sorted(valores)
print(f'Você digitou os valores: {crescent}')