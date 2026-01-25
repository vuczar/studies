import os

def calcular_gorjeta(conta: float, porcentagem: float) -> float:
	"""Calculo do valor nominal baseado na porcentagem fornecida"""
	return conta * porcentagem

def calcular_total(conta: float, gorjeta: float) -> float:
	"""Calculo da soma da gorjeta com o valor original da conta"""
	return conta + gorjeta

def limpo(num: str) -> float:
	"""Limpa as entradas para trocar a virgula(,) por ponto(.) e muda para float"""
	num = num.replace(",", ".").strip()
	return abs(float(num))

def linha():
	"""Imprime uma linha de divisão"""
	print("*" * 53)

def limpa_tela():
	"""Limpa a tela usando comando clear, como estou no mac"""
	print()
	input("Tente novamente! (Digite qualquer tecla para continuar)")
	os.system("clear")
	letreiro()

def imprimir(mensagem: str) -> str:
	"""Adiciona inicio de toda mensagem"""
	nova = str("*\t" + mensagem)
	return nova

def letreiro():
	"""Adiciona um letreito"""
	print("""
	   	
	 █▀▀ █▀█ █▀█ ░░█ █▀▀ ▀█▀ ▄▀█
	 █▄█ █▄█ █▀▄ █▄█ ██▄ ░█░ █▀█
		
	   """)