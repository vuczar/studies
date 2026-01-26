"""
Carlos trabalha em um cartório e precisa validar se um CPF informado pelo cliente tem o formato correto 
antes de prosseguir com o atendimento. O CPF deve conter exatamente 11 dígitos numéricos. Se a entrada 
contiver letras ou qualquer outro caractere que não seja um número, o programa deve exibir uma mensagem 
de erro.

Crie um programa que peça ao usuário um número de CPF e 
verifique se ele tem 11 dígitos e contém apenas números.
"""
from functions import letreiro, limpa, erro, formato

def entrada_usuario() -> str:
	"""Recebe entrada do usuário e retorna cpf validado"""
	while True:	
		entrada = limpa(input("Digite um CPF: "))
		if not entrada.isdigit():
			erro("Erro: Digite somente números")
		elif len(entrada) != 11:
			erro("Erro: CPF precisa de 11 números")			
		else:
			return entrada

def resultado(cpf: str):
	"""Imprime CPF válido"""
	print(f"\nCPF Válido : {formato(cpf)}")

def main():
	"""Indice do programa"""
	letreiro() # letreiro do progrma
	cpf = entrada_usuario() # entrada e validação do que o usuário digitou 
	resultado(cpf) # resultado formatado

if __name__ == "__main__":
	main()