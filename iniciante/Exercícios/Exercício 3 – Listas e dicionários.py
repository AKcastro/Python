alunos = [
    {"nome": "Ana", "notas": [8, 7, 10]},
    {"nome": "Bruno", "notas": [6, 5, 7]},
    {"nome": "Clara", "notas": [9, 8, 10]}
]

# a) Calcule a média de cada aluno e adicione no dicionário
for aluno in alunos:
    notas = aluno["notas"]
    media = sum(notas) / len(notas)
    aluno["media"] = media

# b) Filtre apenas os alunos com média >= 7
alunos_aprovados = [aluno for aluno in alunos if aluno["media"] >= 7]

# Exibe os alunos aprovados com nome e média
print("Alunos aprovados (média >= 7):")
for aluno in alunos_aprovados:
    print(f"{aluno['nome']} - Média: {aluno['media']:.2f}")
