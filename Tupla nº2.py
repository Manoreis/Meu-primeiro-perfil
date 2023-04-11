''' TUPLA
Exercício nº2
Criar duas tuplas de números inteiros e mesclá-las em uma terceira tupla em ordem crescente.'''

tupla1= (10, 7, 9)
tupla2= (6, 4, 10)

print (sorted(tupla1))
print("--"*25)
print (sorted(tupla2))
print("--"*25)
print(sorted(tupla1 + tupla2))
import itertools
resultado = list(itertools.chain(tupla1, tupla2))

