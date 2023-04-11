'''DICIONÁRIO
Exercício nº4
Atualizar o valor de um atributo em um dicionário existente.'''


print("=-" * 30)
genero = {'sexo':'feminino'}
dados_cliente = {'nome': 'Maria', 'idade': 10, 'endereço': 'Rua da feira 80', 'telefone': 978880908}
dados_cliente ['email'] = 'maria@gmail.com'
del dados_cliente['idade']
genero.update(dados_cliente)
print(dados_cliente)