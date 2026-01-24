"""
Paulo está desenvolvendo um programa para calcular valores acumulados em um sistema financeiro. 
Ele precisa somar os todos os números inteiros de 1 até n, onde n é um valor escolhido pelo usuário.

Ajude Paulo criando uma função recursiva que receba um número 
n e retorne a soma de todos os números inteiros de 1 até N.
"""

def soma(multiplicador):
	if multiplicador > 1:
		return multiplicador + soma(multiplicador - 1)
	return multiplicador

numero = int(input("Digite um número : "))
print(f"A soma de 1 a {numero} é : {soma(numero)}")