| Horas de Estudo por Semana | Passou (1=sim, 0=não) |
| -------------------------- | --------------------- |
| 1                          | 0                     |
| 2                          | 0                     |
| 3                          | 0                     |
| 4                          | 0                     |
| 5                          | 1                     |
| 6                          | 1                     |
| 7                          | 1                     |
| 8                          | 1                     |
| 9                          | 1                     |
| 10                         | 1                     |

# Treinar o modelo com os dados acima. Pedir ao usuário quantas horas ele estuda por semana
# Prever se ele vai passar (1) ou não (0). Mostrar a probabilidade de passar
# Mostrar um gráfico com: Pontos reais (azuis). Curva de probabilidade (vermelha)
# Linha vertical com entrada do usuário (verde)

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import numpy as np

# Criando os dados
dados = pd.DataFrame({
    'hora': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'passou': [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
})

# Separando X (entrada) e y (resposta)
X = dados[['hora']].values  # Convertendo para numpy array
y = dados['passou']

# Criando e treinando o modelo
modelo = LogisticRegression()
modelo.fit(X, y)

# Entrada do usuário (garantindo que a entrada seja um numpy array)
hora = float(input("Quantas horas você estuda por semana?: "))
entrada = np.array([[hora]])  # Convertendo para numpy array 2D
resposta_prevista = modelo.predict(entrada)

# Mostrando o resultado
print("Resultado:", "Passou" if int(resposta_prevista[0]) == 1 else "Não passou")

# Gráfico
x_plot = np.linspace(0, 12, 300).reshape(-1, 1)
y_plot = modelo.predict_proba(x_plot)[:, 1]  # Probabilidade de passar

plt.scatter(X, y, color='blue', label='Dados reais')
plt.plot(x_plot, y_plot, color='red', label='Probabilidade de passar')
plt.axvline(hora, color='green', linestyle='--', label=f'{hora} horas')
plt.scatter(hora, resposta_prevista[0], color='orange', s=100, label='Previsão')
plt.xlabel("Horas estudadas")
plt.ylabel("Probabilidade de passar")
plt.title("Classificação: Passou ou Não")
plt.legend()
plt.grid(True)
plt.show()
