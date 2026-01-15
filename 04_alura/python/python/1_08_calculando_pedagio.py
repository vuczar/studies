"""
Fernanda está planejando uma viagem e quer calcular quanto pagará de pedágio. O valor do pedágio depende da distância percorrida:

Até 100 km: R$ 10,00
Entre 100 km e 200 km: R$ 20,00
Acima de 200 km: R$ 30,00
Crie um programa que receba a distância percorrida e informe o valor do pedágio correspondente.
""""

distancia = int(input("Digite a distância percorrida (em km): "))

if distancia <= 100:
    valor = 10.00
elif 100 < distancia <= 200:
    valor = 20.00
else:
    valor = 30.00
print (f"Valor do pedágio: R$ {valor:.2f}")