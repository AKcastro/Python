# Importação de bibliotecas
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Estilo dos gráficos
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

# Carregamento do dataset
df = pd.read_csv(".../movies.csv") #!!!!!!!! Escolha onde salvar e mude o diretório nessa linha

# Análise inicial
print("Informações sobre o dataset:")
print(df.info())

print("\nEstatísticas descritivas:")
print(df.describe())

print("\nValores nulos por coluna:")
print(df.isnull().sum())

# Top 10 filmes por receita
print("\nTop 10 filmes por receita:")
top_filmes = df.sort_values("revenue", ascending=False).head(10)
print(top_filmes[["title", "revenue"]])

plt.figure()
sns.barplot(x="revenue", y="title", data=top_filmes, palette="viridis")
plt.title("Top 10 Filmes por Receita")
plt.xlabel("Receita (USD)")
plt.ylabel("Título do Filme")
plt.tight_layout()
plt.show()

# Relação entre orçamento e receita
plt.figure()
sns.scatterplot(x="budget", y="revenue", data=df, alpha=0.6)
plt.title("Orçamento vs Receita")
plt.xlabel("Orçamento (USD)")
plt.ylabel("Receita (USD)")
plt.tight_layout()
plt.show()

# Análise de lançamentos por ano
# Converte a coluna de data (se existir) e extrai o ano
if "release_date" in df.columns:
    df["release_date"] = pd.to_datetime(df["release_date"], errors='coerce')
    df["release_year"] = df["release_date"].dt.year

    plt.figure()
    sns.countplot(x="release_year", data=df, order=sorted(df["release_year"].dropna().unique()))
    plt.title("Número de Filmes por Ano")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

# Avaliação média por gênero (simples)
if "genres" in df.columns:
    df["main_genre"] = df["genres"].astype(str).str.split(",").str[0]

    plt.figure()
    sns.boxplot(x="main_genre", y="vote_average", data=df)
    plt.title("Avaliação Média por Gênero")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Correlação entre variáveis numéricas
plt.figure()
sns.heatmap(df[["budget", "revenue", "vote_average", "vote_count"]].corr(), annot=True, cmap="coolwarm")
plt.title("Correlação entre Variáveis Numéricas")
plt.tight_layout()
plt.show()
