import matplotlib.pyplot as plt

# Gere 1000 números com distribuição normal
normal = np.random.normal(loc=0, scale=1, size=1000)

plt.hist(normal, bins=30, density=True)
plt.title("Distribuição Normal")
plt.show()
