"""
Beatriz está desenvolvendo um sistema de atendimento para um site de serviços. Ela deseja criar um 
programa que exiba uma saudação personalizada dependendo da hora do dia que o usuário acessa a plataforma. 
O sistema deverá ter a seguinte regra:

Se for antes das 12h, exibir "Bom dia";
Entre 12h e 18h, exibir "Boa tarde";
Após 18h, exibir "Boa noite".
"""

def saudacao(x):
	if 6 < x <= 12:
		return "Buenos dias"
	elif 12 <= x < 18:
		return "Buenas tardes"
	else:
		return "Buenas notches"

hora = int(input("Digite a hora atual (0-23): "))
print(saudacao(hora))