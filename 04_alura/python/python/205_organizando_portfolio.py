"""
Ana está desenvolvendo seu portfólio para exibir os projetos de Python que concluiu. 
Ela organizou uma lista com o nome de cada projeto, mas percebeu que alguns itens 
podem estar ausentes, aparecendo como None:

projetos = ["website", "jogo", "analise de dados", None, "aplicativo movel"]

Crie um programa que ajude Ana a percorrer a lista de projetos e exiba os nomes dos 
projetos válidos. Se encontrar um item None, o programa deve exibir a mensagem: "Projeto ausente".
"""

projetos = ["website", "jogo", "analise de dados", None, "aplicativo movel"]

for x in projetos:
    if x == None:
        print("Projeto ausente")
    else:
        print(x)