'''
João trabalha como garçom em um restaurante e precisa calcular a gorjeta que os clientes deixam ao pagar 
a conta. O restaurante sugere uma gorjeta de 10%, mas alguns clientes podem escolher dar mais ou menos.

Para agilizar o processo, João quer um programa que receba o valor total da conta e 
a porcentagem de gorjeta desejada e exiba o valor final que o cliente deverá pagar.

Crie um programa que peça ao usuário o valor da conta e a porcentagem de gorjeta. 
O programa deve calcular e exibir o valor da gorjeta e o total a ser pago.
'''
from funcoes import calcular_gorjeta, calcular_total, limpo, linha, limpa_tela, imprimir, letreiro

def entradas() -> float:
	"""Capta as entradas do usuário"""
	while True:
		try:
			linha()
			valor_conta = limpo(input(imprimir("Digite o valor da conta    : R$ ")))
			porcentagem_gorjeta = limpo(input(imprimir("Digite o valora da gorjeta : % "))) / 100			
			linha()
			print()
			return valor_conta, porcentagem_gorjeta # Se o usuário digitar corretamente a função acaba aqui
		except ValueError:
			print()
			linha()
			print(imprimir("Erro: Digite números e somente números"))
			linha()
			limpa_tela()

def calculos(conta: float, porcentagem: float) -> float:
	"""Calcula os resultados"""
	valor_gorjeta = calcular_gorjeta(conta, porcentagem)
	total_pagar = calcular_total(conta, valor_gorjeta)
	return total_pagar, valor_gorjeta

def resultados(total: float, gorjeta: float):
	"""Printa os resultados"""
	linha()
	print(f"*\tValor total da gorjeta. : R${gorjeta:.2f}")
	print(f"*\tValor total a pagar.    : R${total:.2f}")
	linha()

def main():
	"""Índice do exercicio"""
	letreiro()
	conta, porcentagem = entradas()
	total, gorjeta = calculos(conta, porcentagem)
	resultados(total, gorjeta)

if __name__ == "__main__":
	main() # Onde tudo começa