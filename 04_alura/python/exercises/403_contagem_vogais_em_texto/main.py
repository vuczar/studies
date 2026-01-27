"""
Mariana é professora de língua portuguesa e quer um programa que conte quantas vogais há em 
um texto digitado pelos alunos. Isso ajudará a analisar a estrutura das palavras utilizadas.

Crie um programa que peça um texto e exiba quantas vogais (a, e, i, o, u) ele contém.
"""

print("""
₀₁₁₁₀₁₁₀₀₁₁₁₀₁₀₁₀₁₁₀₀₀₁₁₀₁₁₁₁₀₁₀₀₁₁₀₀₀₀₁₀₁₁₁₀₀₁₀
	                                                 
                                           _|            
 _|      _|    _|_|      _|_|_|    _|_|_|        _|_|_|  
 _|      _|  _|    _|  _|    _|  _|    _|  _|  _|_|      
   _|  _|    _|    _|  _|    _|  _|    _|  _|      _|_|  
     _|        _|_|      _|_|_|    _|_|_|  _|  _|_|_|    
                             _|                          
                         _|_|                              

""")

x = "A linguagem Python é muito versátil."
vogais = ["a", "e", "i", "o", "u"]
total = 0
for a in x.lower():
	if a in vogais:
		total +=1

print(total)
