#Crie um DataFrame com dados fictícios contendo: Coluna 'hora': horas estudadas por semana.
#Coluna 'nota': nota obtida.
#Coluna 'passou': 0 se reprovou, 1 se passou.
#Treine dois modelos: Um de regressão linear para prever a nota.
#Um de classificação logística para prever se passou.
#Peça para o usuário digitar quantas horas ele estuda por semana.
#Com base na entrada: Mostre a nota prevista.
#Mostre se ele provavelmente passará ou não.
#Exiba um gráfico que:
#Mostra os dados reais.
#Mostra a reta de regressão (notas).
#Mostra a curva de probabilidade de passar.

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression, LinearRegression
import numpy as np

# Criando os dados
dados = pd.DataFrame({
    'hora': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'nota': [2.0, 3.0, 4.0, 4.5, 6.0, 7.0, 7.5, 8.5, 9.0, 10.0],
    'passou': [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
})

# Separando X e y
X = dados[['hora']]
y_class = dados['passou']
y_reg = dados['nota']

# Treinando os modelos
modelo_log = LogisticRegression()
modelo_log.fit(X, y_class)

modelo_lin = LinearRegression()
modelo_lin.fit(X, y_reg)

# Entrada do usuário
hora = float(input("Quantas horas você estuda por semana?: "))
entrada = pd.DataFrame({'hora': [hora]})

# Previsões
prob_passar = modelo_log.predict_proba(entrada)[0][1]
classificacao = modelo_log.predict(entrada)[0]
nota_prevista = modelo_lin.predict(entrada)[0]

# Saída
print(f"\nNota prevista: {nota_prevista:.2f}")
print(f"Probabilidade de passar: {prob_passar * 100:.2f}%")
print("Classificação:", "Passou" if classificacao == 1 else "Não passou")

# Gráfico
x_plot = pd.DataFrame({'hora': np.linspace(0, 12, 300)})
y_reg_plot = modelo_lin.predict(x_plot)
y_log_plot = modelo_log.predict_proba(x_plot)[:, 1]

plt.figure(figsize=(12, 5))

# Subplot 1 - Regressão linear (nota)
plt.subplot(1, 2, 1)
plt.scatter(X, y_reg, color='blue', label='Notas reais')
plt.plot(x_plot, y_reg_plot, color='red', label='Nota prevista')
plt.axvline(hora, color='green', linestyle='--', label=f'{hora}h')
plt.scatter(hora, nota_prevista, color='orange', s=100, label='Sua nota')
plt.xlabel("Horas estudadas")
plt.ylabel("Nota")
plt.title("Regressão Linear: Horas vs Nota")
plt.legend()
plt.grid(True)

# Subplot 2 - Classificação logística
plt.subplot(1, 2, 2)
plt.scatter(X, y_class, color='blue', label='Dados reais')
plt.plot(x_plot, y_log_plot, color='purple', label='Probabilidade de passar')
plt.axvline(hora, color='green', linestyle='--', label=f'{hora}h')
plt.scatter(hora, prob_passar, color='orange', s=100, label='Sua probabilidade')
plt.xlabel("Horas estudadas")
plt.ylabel("Probabilidade de passar")
plt.title("Classificação Logística")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
