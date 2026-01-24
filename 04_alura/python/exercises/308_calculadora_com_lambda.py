"""
Joana está participando de um processo seletivo para uma vaga de desenvolvedora e recebeu um desafio 
técnico de criar uma calculadora para somar, subtrair, multiplicar e dividir dois números.

Sua tarefa é criar um programa usando funções lambda que receba dois números e um operador matemático 
escolhido pelo usuário (+, -, * ou /) e exiba o resultado correspondente.
"""

soma = lambda x,y: x + y
subtracao = lambda x,y: x - y
multiplicacao = lambda x, y: x * y
divisao = lambda x,y: x / y

numero1 = float(input("Digite o primeiro número : "))
numero2 = float(input("Digite o segundo número : "))
operacao = input("Escolha a operação ( + - * / ) : ")

if operacao == "+":
	print(f"O resultado é : {soma(numero1, numero2)}")

elif operacao == "-":
	print(f"O resultado é : {subtracao(numero1, numero2)}")

elif operacao == "*":
	print(f"O resultado é : {multiplicacao(numero1, numero2)}")

elif operacao == "/":
	if numero1 == 0 or numero2 == 0:
		print("O resulto é : Infiny and beyond")
	else:
		print(f"O resultado é : {divisao(numero1, numero2):.2f}")
else:
	print("Digitou outra coisa, menos uma operação")