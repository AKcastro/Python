# Estudando estruturas condicionais em Python

# Texto explicativo:
# Condicionais são usadas para executar diferentes blocos de código
# dependendo de condições verdadeiras ou falsas.

# Exemplo básico de if
idade = 18

if idade >= 18:
    print("Você é maior de idade!")

# Exemplo de if-else
nota = 6

if nota >= 7:
    print("Aprovado!")
else:
    print("Reprovado!")

# Exemplo de if-elif-else
temperatura = 25

if temperatura > 30:
    print("Está muito quente!")
elif temperatura > 20:
    print("O clima está agradável.")
else:
    print("Está frio.")

# Usando operadores lógicos (and, or, not)
# Vamos ver se um aluno passou em duas matérias
nota_matematica = 8
nota_portugues = 5

if nota_matematica >= 7 and nota_portugues >= 7:
    print("Aluno aprovado em ambas as matérias!")
else:
    print("Aluno não passou em todas as matérias.")

# Dica:
# Em Python, cuidado com a indentação! (4 espaços ou tabulação correta)

# Exercício proposto:
# Peça ao usuário sua idade (input) e diga se ele pode ou não dirigir.

Código:
# Solicita a idade do usuário
idade = int(input("Digite sua idade: "))

# Verifica se o usuário pode dirigir
if idade >= 18:
    print("Pode dirigir!")
else:
    print("Sinto muito, você ainda não pode dirigir.")
