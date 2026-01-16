"""
Pedro está criando um sistema de cadastro de produtos para sua loja e percebeu que todos 
os números de telefone dos clientes estão armazenados como strings. No entanto, para 
facilitar buscas e validações, ele precisa que esses números sejam tratados como inteiros.

Dado o seguinte código com uma lista de números de telefone armazenados incorretamente 
como str, faça duas funções, uma que converte os tipos para inteiro e outra que verifica
se a conversão foi feita corretamente e todos os números de telefone são inteiros:
"""

def converter(lista):
	return [int(x) for x in lista]

def check(lista):
	for y in lista:
		if not isinstance(y, int):
			return "Erro na conversão"
		else:
			return "Todos os números foram convertidos corretamente!"

lista_telefones = ["11987654321", "21912345678", "31987654321", "11911223344"]

nova_lista = converter(lista_telefones)
print(f"Antiga lista: {lista_telefones}\nLista nova: {nova_lista}")
print(check(nova_lista))