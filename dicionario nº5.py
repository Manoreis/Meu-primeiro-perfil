'''DICIONÁRIO
Exercício nº5
Contar o número de itens em um dicionário.'''


print("=-" * 30)
dados_cliente = {'nome': 'Maria', 'idade': 10, 'endereço': 'Rua da feira 80', 'telefone': 978880908}

def count_keys(dados_cliente):
    count = 0
    for i in enumerate(dados_cliente):
        count += 1
    return count

print(count_keys(dados_cliente))