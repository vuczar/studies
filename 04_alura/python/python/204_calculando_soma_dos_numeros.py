"""
Você está recebendo uma lista de valores representando os produtos de sua loja virtual e gostaria 
de calcular a soma total desses produtos para entender o desempenho financeiro semanal.
"""

valores = [10, 20, 30, 40, 50]
resultado = 0
for x in valores:
    resultado += x
print(f"A soma total das receitas é: {resultado}")