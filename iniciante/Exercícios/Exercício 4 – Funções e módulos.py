# Crie uma função que calcule a média de uma lista
def calcular_media(lista):
    return sum(lista)/len(lista)

# Medidas descritivas: Média, Mediana, Moda, Variância, Desvio Padrão
import numpy as np
from scipy import stats

dados = [10, 15, 14, 10, 18, 20, 15, 10]

# a) Calcule a média, mediana e moda
print("Média:", np.mean(dados))
print("Mediana:", np.median(dados))
print("Moda:", stats.mode(dados, keepdims=True).mode[0])

# b) Calcule a variância e desvio padrão
print("Variância:", np.var(dados, ddof=1))  # amostral
print("Desvio padrão:", np.std(dados, ddof=1))
