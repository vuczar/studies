import os

def letreiro():
	os.system("clear")
	print("""
	  _____  ___    ____
	 / ___/ / _ \  / __/
 	/ /__  / ___/ / _/  
	\___/ /_/    /_/    
	
	""")

def limpa(entrada: str) -> str:
	"""Recebe uma str, retira pontuação e valores espaços em brancos"""
	return entrada.replace(".", "").replace("-", "").strip()

def erro(mensagem: str):
	print()
	input(mensagem + "\n\n(Tecle ENTER para continuar)...")
	letreiro()

def formato(num: str) -> str:
	"""Recebe a str '123456789' e retorna com a máscara de CPF '123.456.789-01' """
	return f"{num[:3]}.{num[3:6]}.{num[6:9]}-{num[9:]}"