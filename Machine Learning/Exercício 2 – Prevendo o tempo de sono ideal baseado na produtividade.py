| Horas de Sono | Produtividade (de 0 a 10) |
| ------------- | ------------------------- |
| 3             | 2.0                       |
| 4             | 3.0                       |
| 5             | 4.5                       |
| 6             | 6.0                       |
| 7             | 8.0                       |
| 8             | 9.0                       |
| 9             | 9.2                       |
| 10            | 8.5                       |
| 11            | 7.0                       |


# Treinar um modelo de regressão linear para prever a produtividade com base nas horas de sono.
# Pedir ao usuário quantas horas ele costuma dormir por noite.
# Prever a produtividade correspondente.

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Criando os dados
dados = pd.DataFrame({
    'hora': [3, 4, 5, 6, 7, 8, 9, 10, 11],
    'produtividade': [2.0, 3.0, 4.5, 6.0, 8.0, 9.0, 9.2, 8.5, 7.0]
})

# Separando X (entrada) e y (resposta)
X = dados[['hora']]
y = dados['produtividade']

# Criando e treinando o modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Entrada do usuário
hora = float(input("Quantas horas você dorme por noite?:"))
entrada = pd.DataFrame({'hora': [hora]})
produtividade_prevista = modelo.predict(entrada)

# Mostrando o resultado
print(f"Produtividade prevista: {produtividade_prevista[0]:.2f}")

# Gráfico
plt.scatter(X, y, color='blue', label='Dados reais')
plt.plot(X, modelo.predict(X), color='red', label='Regressão Linear')
plt.axvline(hora, color='green', linestyle='--', label=f'{hora} horas')
plt.xlabel("Horas dormidas")
plt.ylabel("Produtividade")
plt.title("Horas dormidas vs produtividade")
plt.legend()
plt.grid(True)
plt.show()
