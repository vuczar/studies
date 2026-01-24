"""
Miguel está desenvolvendo um sistema de cupons de desconto e precisa de uma 
forma para aplicar diferentes taxas de desconto sobre os valores das compras.

Diante deste problema, crie uma closure que gere uma função capaz 
de calcular o preço final com um desconto fixo definido pelo usuário.
"""

def criar_cupom(porcentagem):
	def aplicar_desconto(compra):
		return compra * (1 - (porcentagem / 100)) 
	return aplicar_desconto

porcentagem = float(input("Digite a porcentagem de desconto : "))
compra = float(input("Digite o valor da compra : "))

cupom = criar_cupom(porcentagem)
valor_final = cupom(compra)

print (f"Preço final com desconto: {valor_final}")