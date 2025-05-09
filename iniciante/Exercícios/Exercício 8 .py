#Peça ao usuário que digite o nome de um gênero (ex: Ação, Romance, etc.)
#Filtre o DataFrame para mostrar apenas os filmes desse gênero.
#Crie uma nova coluna chamada avaliacao, onde: Nota ≥ 8 → "Excelente"
#Nota ≥ 6 → "Boa"
#Menor que 6 → "Ruim"
#Mostre: A quantidade de filmes por avaliação nesse gênero.
#A média das notas nesse gênero.
#O filme com a maior nota nesse gênero.
#Se a média da avaliação "Boa" for exatamente 7.9, imprima: "Categoria 'Boa' com média perfeita!"

import pandas as pd

# Carregando o DataFrame
df = pd.read_csv(".../filmes.csv")

# Função para classificar a nota
def classificacao(n):
    if n >= 8:
        return "Excelente"
    elif n >= 6:
        return "Boa"
    else:
        return "Ruim"

# Entrada do usuário
filme = input("Digite o nome de um gênero: ").lower()

# Filtrando e copiando o DataFrame
df_genero = df[df["genero"].str.lower() == filme].copy()
print("\n")

# Aplicando a classificação
df_genero["avaliacao"] = df_genero["nota"].apply(classificacao)

# Exibindo os filmes do gênero informado
print(df_genero)

# Contando quantos filmes por categoria
print("\nQuantidade por categoria:")
print(df_genero["avaliacao"].value_counts())

# Média das notas por categoria
print("\nMédia das notas por categoria:")
print(df_genero.groupby("avaliacao")["nota"].mean())

# Melhor filme do gênero
melhor_filme = df_genero.sort_values("nota", ascending=False).head(1)
print("\nFilme com a maior nota:")
print(melhor_filme)

# Exibindo se há média "perfeita" (7.9) na categoria "Boa"
media_boas = df_genero[df_genero["avaliacao"] == "Boa"]["nota"].mean()
if media_boas == 7.9:
    print("\nCategoria 'Boa' com média perfeita!")
    print(df_genero[df_genero["avaliacao"] == "Boa"])
