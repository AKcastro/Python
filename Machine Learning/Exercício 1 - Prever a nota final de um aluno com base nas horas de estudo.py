| Horas de Estudo por Semana | Nota Final |
| -------------------------- | ---------- |
| 1                          | 4.0        |
| 2                          | 5.0        |
| 3                          | 6.0        |
| 4                          | 6.5        |
| 5                          | 7.0        |
| 6                          | 8.0        |
| 7                          | 8.5        |
| 8                          | 9.0        |
| 9                          | 9.5        |
| 10                         | 10.0       |

# Proposta: Treinar um modelo de regressão linear com esses dados. Pedir ao usuário quantas horas ele estuda por semana.
# Prever a nota que ele teria com base no modelo. Mostrar um gráfico com os pontos reais e a linha de previsão.

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Criando os dados
dados = pd.DataFrame({
    'hora': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'nota': [4.0, 5.0, 6.0, 6.5, 7.0, 8.0, 8.5, 9.0, 9.5, 10.0]
})

# Separando X (entrada) e y (resposta)
X = dados[['hora']]
y = dados['nota']

# Criando e treinando o modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Entrada do usuário
hora = float(input("Quantas horas você estuda por semana?:"))
entrada = pd.DataFrame({'hora': [hora]})
nota_prevista = modelo.predict(entrada)

# Mostrando o resultado
print(f"Nota prevista: {nota_prevista[0]:.2f}")

# Gráfico
plt.scatter(X, y, color='blue', label='Dados reais')
plt.plot(X, modelo.predict(X), color='red', label='Regressão Linear')
plt.axvline(hora, color='green', linestyle='--', label=f'{hora} horas')
plt.xlabel("Horas estudadas")
plt.ylabel("Nota")
plt.title("Horas estudadas vs notas")
plt.legend()
plt.grid(True)
plt.show()
