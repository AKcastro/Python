Objetivo: Criar um modelo que diga se um aluno está aprovado ou reprovado com base em sua nota final.

1. Lógica do projeto:
Entrada: nota final do aluno
Saída: 1 para aprovado (nota ≥ 6), 0 para reprovado

Código: 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import numpy as np

dados = pd.DataFrame({
    'notas':     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'reprovacao':[1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
})

# Treinamento
X = dados[['notas']]
y = dados['reprovacao']
modelo = LogisticRegression()
modelo.fit(X, y)

# Entrada do usuário
nota_usuario = float(input("Digite a nota do aluno (0 a 10): "))

# Previsão
entrada = pd.DataFrame({'notas': [nota_usuario]})
reprovacao = modelo.predict(entrada)
probabilidade = modelo.predict_proba(entrada)

# Resultado da previsão
print("Resultado previsto:", "Reprovado" if reprovacao[0] == 1 else "Aprovado")
print(f"Probabilidade de reprovação: {probabilidade[0][1]*100:.2f}%")

# Gráfico (Caso não queira o gráfico é so colocar as aspas duplas(""" """)
x_plot = pd.DataFrame(np.linspace(0, 10, 100), columns=['notas'])
y_plot = modelo.predict_proba(x_plot)[:, 1]

plt.scatter(X, y, color='blue', label='Dados Reais')
plt.plot(x_plot, y_plot, color='red', label='Probabilidade de Reprovação')
plt.axvline(nota_usuario, color='green', linestyle='--', label=f'Nota {nota_usuario} (teste)')
plt.xlabel("Nota")
plt.ylabel("Probabilidade de Reprovação")
plt.title("Classificação: Aprovado ou Reprovado")
plt.legend()
plt.grid(True)
plt.ylim(-0.1, 1.1)
plt.show()
