'''DICIONÁRIO
Exercício nº3
Remover um item de um dicionário existente.'''

print("=-" * 30)
dados_cliente = {'nome': 'Maria', 'idade': 10, 'endereço': 'Rua da feira 80', 'telefone': 978880908}
dados_cliente ['email'] = 'maria@gmail.com'
del dados_cliente['idade']
print(dados_cliente)
