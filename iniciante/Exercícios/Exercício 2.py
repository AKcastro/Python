Operações básicas:
Adição	+	
Subtração	-	
Multiplicação	*	
Divisão	/	(sempre retorna número decimal (float)).
Divisão inteira	// (corta as casas decimais e deixa só o número inteiro).
Resto da divisão (módulo)	%	(é MUITO usado para descobrir coisas como números pares e ímpares).
Potência	**	

Exercício 2: Pergunte para o usuário dois números (use input()) e calcule: A soma, a subtração, a multiplicação, a divisão, o resto da divisão, a potência do primeiro número elevado ao segundo e imprima todos os resultados.

Código: 
numero1 = float(input("Digite o primeiro número (use ponto ao invés de vírgula): "))
numero2 = float(input("Digite o segundo número (use ponto ao invés de vígula): "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2
resto = numero1 % numero2
potencia = numero1 ** numero2

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
print("Resto da divisão:", resto)
print("Potência:", potencia)
