'''TUPLA
Exercício nº 5
Criar uma tupla com números inteiros e contar quantos números pares e quantos números ímpares existem na tupla.'''

print( '=-' * 22)
tupla = (1, 2, 4, 0, 3, 7, 9, 6, 5, 10, 11, 13, 15)
print(sorted(tupla))
print( '=-' * 22)
def qtd_impares (tupla):
    return len([n for n in tupla if n % 2 != 0])

def qtd_pares (tupla):
    return len([n for n in tupla if n % 2 == 0])

print("quantidade de números ímpares = ", qtd_impares(tupla))
print( '=-' * 22)
print("quantidade de números pares = ", qtd_pares(tupla))