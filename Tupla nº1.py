'''TUPLA
Exercício nº 1
Criar uma tupla com 10 números inteiros aleatórios e imprimir o maior e o menor número da tupla.'''


from random import randint
números = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end= '')
for n in números:
    print(f' {n} ', end='')

print( f'\n O maior valor sorteado na tupla foi: {max (números)}')
print('=-' *30)
print( f'O menor valor sorteado na tupla foi: {min (números)}')