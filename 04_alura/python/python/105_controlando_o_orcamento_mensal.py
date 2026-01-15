orcamento = float(input("Digite o total de despesas do mês (R$): "))
print("Atenção! Você ultrapassou o limite do orçamento" if orcamento > 3000 else "Você ainda está dentro do limite")