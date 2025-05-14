# Remover a coluna 'nome' (não é útil para o modelo).
# Preencher: Valores nulos em idade e salario com a média da coluna.
# Valores nulos em genero com o valor mais frequente.
# Codificar as variáveis categóricas (genero, cidade) usando OneHotEncoder.
# Normalizar as variáveis numéricas (idade, salario) usando StandardScaler.
# Separar os dados em X (entradas) e y (resposta).
# Dividir os dados em treino e teste com train_test_split.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

dados = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo', None],
    'idade': [23, None, 35, 29, None, 40],
    'genero': ['F', 'M', 'M', None, 'M', 'F'],
    'salario': [3200, 4000, 5000, 4200, 3900, None],
    'cidade': ['SP', 'RJ', 'SP', 'MG', 'SP', 'RJ'],
    'comprou': [1, 0, 1, 0, 1, 0]
})

print("---- Dados Originais ----")
print(dados)

# Removendo a coluna 'nome' que não será usada
X = dados.drop(columns=['comprou', 'nome'])
y = dados['comprou']

# Atualizando listas de colunas
colunas_numericas = ['idade', 'salario']
colunas_categoricas = ['genero', 'cidade']

pipeline_numerico = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),  # Preencher valores nulos com média
    ('scaler', StandardScaler())  # Normalizar
])

pipeline_categorico = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),  # Preencher com valor mais comum
    ('onehot', OneHotEncoder(handle_unknown='ignore'))  # Codificação
])
preprocessador = ColumnTransformer(transformers=[
    ('num', pipeline_numerico, colunas_numericas),
    ('cat', pipeline_categorico, colunas_categoricas)
])

x_procesado = preprocessador.fit_transform(X)

x_treino, X_teste, y_treino, y_teste = train_test_split(x_procesado, y, test_size=0.2, random_state=42)

print("\n---- Dados Prontos para o Modelo ----")
print(x_treino)
