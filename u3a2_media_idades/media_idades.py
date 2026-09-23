import pandas as pd

dados = {
    'Nome': ['Alice', 'Bob', 'Carol', 'David', 'Eve'],
    'Idade': [25, 30, 22, 35, 28]
}

serie_idades = pd.Series(dados['Idade'], index=dados['Nome'])
print("Série de Idades:")
print(serie_idades)

media_idades = serie_idades.mean()
print("\nMédia de Idades:", media_idades)