import pandas as pd

livros = ['Literatura Brasileira', 'Literatura Estrangeira', 'Ciências', 'Matemática', 'História']
qtd_estoque = [12, 9, 18, 14, 20]

estoque = pd.Series(qtd_estoque, index=livros)

estoque.loc['Filosofia'] = None

qtd_emprestados = pd.Series([4, 5, 7, 5, 6], index=livros)

qtd_diponivel = pd.Series((qtd_estoque - qtd_emprestados), index=livros)

print(f'Livros com estoque maior que 5:\n{qtd_diponivel[qtd_diponivel > 5]}')
