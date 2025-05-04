Exercício 1: Criar uma variável chamada cidade que guarde o nome de uma cidade (ex: "São Paulo"), uma variável chamada populacao que guarde o número de habitantes (ex: 12300000), uma variável chamada temperatura_media que guarde a temperatura média da cidade (ex: 23.5), imprima todas essas variáveis usando print() e mostre o tipo de cada variável usando type().

Código:
cidade = input("Digite o nome da cidade: ") #Recebe a informação do usuário.
populacao = input("Digite o número da população (Número inteiro sem pontuação):  ")
temperatura_media = float(input("Digite a temperatura média: "))

print(cidade) #Mostra o que foi digitado
print(populacao)
print(temperatura_media,"°C")

print(type(cidade)) #Mostra os tipos das variáveis
print(type(populacao))
print(type(temperatura_media))
