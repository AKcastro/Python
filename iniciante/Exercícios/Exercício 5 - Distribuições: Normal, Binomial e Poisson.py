# Normal
import matplotlib.pyplot as plt

# Gere 1000 números com distribuição normal
normal = np.random.normal(loc=0, scale=1, size=1000)

plt.hist(normal, bins=30, density=True)
plt.title("Distribuição Normal")
plt.show()

# Binomial
binomial = np.random.binomial(n=10, p=0.5, size=1000)

plt.hist(binomial, bins=10)
plt.title("Distribuição Binomial (n=10, p=0.5)")
plt.show()

# Poisson
poisson = np.random.poisson(lam=3, size=1000)

plt.hist(poisson, bins=15)
plt.title("Distribuição de Poisson (λ=3)")
plt.show()

