a = int(input("Informe os dias para a atividade A: "))
b = int(input("Informe os dias para a atividade B: "))
c = int(input("Informe os dias para a atividade C: "))
if a < 0 or b < 0 or c < 0:
    print("Erro: Os dias não podem ser negativos")
else:
    print(f'O total de dias é : {a + b + c}')