def multiplicar(y):
	def calcular(x):
		return x * y
	return calcular

dobro = multiplicar(2)
triplo = multiplicar(3)

print(f"O dobro de 4 é {dobro(4)}")
print(f"O triplo de 4 é {triplo(4)}")