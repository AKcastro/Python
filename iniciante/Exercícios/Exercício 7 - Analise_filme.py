import pandas as pd  # Importa a biblioteca pandas

# Lê o arquivo CSV e armazena na variável df
df = pd.read_csv("C:/Users/akami/OneDrive/Área de Trabalho/vscode/filmes.csv") 

# Mostra as 3 primeiras linhas
print("As 3 primeiras linhas da tabela:")
print(df.head(3))

# Filtra os filmes com nota acima de 8
filmes_bons = df[df["nota"] > 8]
print("\nFilmes com nota acima de 8:")
print(filmes_bons)

# Mostra só os filmes do gênero "Romance"
print("\nFilmes de Romance:")
print(df[df["genero"] == "Romance"])

# Mostra os filmes ordenados da maior para a menor nota
print("\nFilmes ordenados da maior para a menor nota:")
print(df.sort_values("nota",ascending=False))

# Mostra quantos filmes tem de cada gênero
print("\nFilmes de cada gênero:")
print(df["genero"].value_counts())

# Cria uma nova coluna chamada avaliacao: Se a nota for maior ou igual a 8 → "Excelente"
# Se a nota for entre 6 e 7.9 → "Boa"
# Se a nota for menor que 6 → "Ruim"
print("\nTabela com a avaliação:")
def classificacao_nota(n): 
    if n >= 8: 
        return "Excelente"
    elif n >= 6:
        return "Boa"
    else:
        return "Ruim"
    
# Mostra a média da nota por avaliação (e não por gênero).
df["avaliacao"] = df["nota"].apply(classificacao_nota) 
print(df) 
print("\n")
print(df.groupby("avaliacao")["nota"].mean()) 

# Mostra quantos filmes existem em cada categoria de avaliação.
print("\nQuantidade de fimes existentes na categoria avaliação:") 
print(df["avaliacao"].value_counts())
