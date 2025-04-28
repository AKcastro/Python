# Estudando variáveis em Python

# Texto explicativo:
# Em Python, uma variável é criada no momento em que você atribui um valor a ela.

# Atribuindo diferentes tipos de valores a variáveis:
nome = "Violet"         # tipo str (string)
idade = 25            # tipo int (inteiro)
altura = 1.75         # tipo float (número decimal)
estudante = True      # tipo bool (booleano)

# Exibindo os valores
print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura, "m")
print("É estudante?", estudante)

# Dica: você pode usar a função type() para descobrir o tipo da variável:
print("\nTipos das variáveis:")
print("nome:", type(nome))
print("idade:", type(idade))
print("altura:", type(altura))
print("estudante:", type(estudante))

# Exemplo de múltiplas atribuições:
x, y, z = 10, 20, 30
print("\nMúltiplas atribuições:", x, y, z)

# Exercício proposto:
# Crie suas próprias variáveis e imprima o tipo delas!

Código:
# Coletando informações do usuário
cidade = input("Digite o nome da cidade: ")  # input já é string

# Tentando converter os valores diretamente 
populacao = int(input("Digite o número da população (número inteiro sem pontuação): "))
temperatura_media = float(input("Digite a temperatura média (em °C): "))

# Exibindo os dados coletados
print("\nDados coletados:")
print("Cidade:", cidade)
print("População:", populacao)
print("Temperatura média:", temperatura_media, "°C")

# Mostrando o tipo das variáveis
print("\nTipos das variáveis:")
print("cidade:", type(cidade))
print("populacao:", type(populacao))
print("temperatura_media:", type(temperatura_media))


