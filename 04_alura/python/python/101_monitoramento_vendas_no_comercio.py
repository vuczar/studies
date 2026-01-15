qtd_maca = input("Digite a quantidade de maçãs vendadas: ")
qtd_bananas = input("Digite a quantidade de bananas vendidas: ")

if qtd_maca == qtd_bananas:
    print("O número de vendas são iguais!")
else:
    print("As maças tiveram mais vendas" if qtd_maca > qtd_bananas else "As bananas tiveram mais vendas")