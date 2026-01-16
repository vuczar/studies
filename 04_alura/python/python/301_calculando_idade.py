"""
Julia é professora e precisa de um programa para ajudar seus alunos a calcularem suas idades com
base no ano de nascimento. Sua tarefa é criar uma função que receba o ano de nascimento e o ano 
atual e retorne à idade correspondente.
"""

ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

def calculo(a, b):
	return a - b

print(f"A idade é {calculo(ano_atual,ano_nascimento)} anos.")