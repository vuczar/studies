"""
Lucas está desenvolvendo um sistema para gerar relatórios financeiros e precisa 
filtrar apenas os valores pares de uma lista de números informada pelo usuário.

Crie um programa que receba uma lista de números e exiba apenas os pares usando a função filter().
"""

def converter(lista):
	return [int(x) for x in lista]

numeros = input("Digite os números (separados): ").split()
nova_lista = converter(numeros)
print(nova_lista)