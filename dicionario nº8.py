'''DICIONÁRIO
Exercício nº8
percorrer todos os itens em um dicionário e imprimir os atributos e valores.'''

print("=-" * 30)
dados_cliente = {'nome': 'Maria', 'idade': 10, 'endereço': 'Rua da feira 80', 'telefone': 978880908}
print(dados_cliente ['nome'])
print( 'telefone' in dados_cliente )
print('=-' *30)
print('O número em questa existe na lista! ')

for chave in dados_cliente.keys():
  print(f'Chave = {chave} e Valor = {dados_cliente[chave]}')
