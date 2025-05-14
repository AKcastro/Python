# Remover a coluna 'nome' (não é útil para o modelo).
# Preencher: Valores nulos em idade e salario com a média da coluna.
# Valores nulos em genero com o valor mais frequente.
# Codificar as variáveis categóricas (genero, cidade) usando OneHotEncoder.
# Normalizar as variáveis numéricas (idade, salario) usando StandardScaler.
# Separar os dados em X (entradas) e y (resposta).
# Dividir os dados em treino e teste com train_test_split.

import pandas as pd # pandas: biblioteca para manipular dados em tabelas (DataFrame).
from sklearn.model_selection import train_test_split # train_test_split: separa os dados em treino e teste.
from sklearn.preprocessing import OneHotEncoder, StandardScaler # OneHotEncoder: transforma texto (categorias) em números binários. StandardScaler: normaliza dados numéricos para uma escala padrão.
from sklearn.compose import ColumnTransformer # ColumnTransformer: aplica transformações diferentes em colunas específicas.
from sklearn.pipeline import Pipeline # Pipeline: encadeia várias etapas de pré-processamento.
from sklearn.impute import SimpleImputer # SimpleImputer: preenche valores ausentes (nulos).

dados = pd.DataFrame({ # Cria uma tabela com informações de pessoas, como nome, idade, salário etc.
    'nome': ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo', None],
    'idade': [23, None, 35, 29, None, 40],
    'genero': ['F', 'M', 'M', None, 'M', 'F'],
    'salario': [3200, 4000, 5000, 4200, 3900, None],
    'cidade': ['SP', 'RJ', 'SP', 'MG', 'SP', 'RJ'],
    'comprou': [1, 0, 1, 0, 1, 0] # A coluna comprou será a variável que o modelo tentará prever.
})

print("---- Dados Originais ----")
print(dados)

X = dados.drop(columns=['comprou', 'nome']) # X: são as colunas que explicam o resultado (idade, genero, etc.). A coluna nome foi removida porque não ajuda no modelo.
y = dados['comprou'] # y: é o que queremos prever (comprou -> 1 ou 0).

# Atualizando listas de colunas
colunas_numericas = ['idade', 'salario'] # informa quais colunas têm números (precisam de normalização e imputação média).
colunas_categoricas = ['genero', 'cidade'] # E quais são categorias (precisam de codificação e imputação frequente).

pipeline_numerico = Pipeline(steps=[ # Preenche valores ausentes com a média. Escala os valores para terem média 0 e desvio 1.
    ('imputer', SimpleImputer(strategy='mean')),  # Preencher valores nulos com média
    ('scaler', StandardScaler())  # Normalizar
])

pipeline_categorico = Pipeline(steps=[ # Preenche valores ausentes com o valor mais frequente. Converte texto em números binários com o OneHotEncoder.
    ('imputer', SimpleImputer(strategy='most_frequent')),  # Preencher com valor mais comum
    ('onehot', OneHotEncoder(handle_unknown='ignore'))  # Codificação
])
preprocessador = ColumnTransformer(transformers=[ # Cria um transformador que aplica cada pipeline (numérico ou categórico) nas colunas corretas. Junta tudo para ser aplicado ao mesmo tempo com fit_transform.
    ('num', pipeline_numerico, colunas_numericas),
    ('cat', pipeline_categorico, colunas_categoricas)
])

x_procesado = preprocessador.fit_transform(X) # Aplica todo o processo de tratamento (imputação, normalização, codificação) aos dados. O resultado é um novo conjunto de dados pronto para treinar modelos.

x_treino, X_teste, y_treino, y_teste = train_test_split(x_procesado, y, test_size=0.2, random_state=42) # Divide os dados: 80% para treinar o modelo (x_treino, y_treino), 20% para testar o modelo (X_teste, y_teste), random_state=42 garante que os dados sempre se dividam da mesma forma.

print("\n---- Dados Prontos para o Modelo ----")
print(x_treino) # Mostra os dados já tratados (sem nulos, codificados, normalizados) prontos para entrar em um modelo de machine learning.
