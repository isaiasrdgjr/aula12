import pandas as pd

produtos = ['Notebook', 'Smartphone', 'Tablet', 'Smartwatch', 'Câmera']
qtd_estoque = [15, 30, 20, 10, 25]

estoque = pd.Series(qtd_estoque, index=produtos)

print(5*'=', 'Série Estoque de Produtos', 5*'=')
# print(estoque)


# print(estoque['Notebook'])

# print(estoque[['Notebook', 'Câmera']].values)

print(estoque[estoque >= 20])

print(estoque + 5)

estoque.loc['Headphone'] = None

print(estoque)

precos = pd.Series([3500, 2500, 1200, 900, 1500], index=produtos)

print(precos * estoque)
