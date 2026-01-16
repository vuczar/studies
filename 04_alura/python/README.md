<p><em>PT Este documento é um resumo feito durante o curso de 'Python: Crie seu primeiro app'. São notas pessoais.</em></p>
<p><em>EN This document is a summary made during the 'Python: Build your first app' course. These are personal notes.</em></p>

<h1>Python</h1>

<div align = "center">
	<h2>Notas</h2>
</div>


- CASE PATTERNS
	- 'snakecase': variaveis, funcoes e métodos
	- 'PascalCase': classes
	- 'SCREAMING_CASE': constantes

---
- ASPAS
	- Pode se usar as simples ' ', duplas " ", e triplas """ """
	- A tripla envia tudo que estiver dentro, até quebra de linha.

---
- INTERPOLAÇÃO VARIÁVEIS
	- f-string :
		```python
		print(f"I'm {age} years old.")
		```

	- .format :
		```python
		print("I'm {} years old.".format(age))
		```
	- % string antiga : <code></code>
		```python
		print("I'm %i years old."%(age))
		```

---
- FORMATAÇÃO PRINT
	- <code>sep='\n'</code> : sep determina a separação no print
		```python
		- print('A','L','U','R','A',sep='\n')
		```
	- <code>end=""</code> : end determina o final do print
		```python
		print("O início do termianl deve começar na mesma linha ->", end="")
		```

---
- FORMATAÇÃO NUMEROS
	- f-string : pode ser usado para formatar numeral
		```python
		print(f'O valor arredondado de pi é: {pi:.2f}')
		```
	- .format : outra opção de formatação
		```python
		print('O valor arredondado de pi é: {:.2f}'.format(pi))
		```
	- round : pode ser outra opção
		```python
		print('O valor arredondado de pi é:', round(pi, 2))
		```
---
- INT STR
	- Lembrar de converter o formato ao usar <code>input()</code>
		```python	
		int(input("Digite sua idade: "))
		```
    - Use <code>print(type())</code> sempre que precisar identificar

---
- BIBLIOTECAS
	- Usar <code>import</code> para isso no início do código
	- Existem diversas bibliotecas uteis como 'os', 'math'

---
- LISTAS TUPLAS DICITONARY
	- Listas : mutável</li>
		- Use [ ] para declarar : <code>variavel = []</code>
	- Tuplas : não mutável
		- Use ( ) para declarar : <code>variavel = ()</code>

---
- IF,ELIF,ELSE
	- Pode se fazer de forma estruturada ou ternário</li>
		```python
		if a % 2:
			print("even")
		elif a % 2 and a > 1:
			print("even with one divisor")
		else:
			print("odd")
        ```
		
		```python
		print("hot" if temperature > 30 else "not too hot" )
		```
---
- FOR AND WHILE
	- For
		```python
		for nome in nomes:
			print(nome)
		```
		- para cada elemento dentro do iterável(nomes), a variável (nome) recebe o valor do elemento

	- While
		```python
        while number < 3:
			print(number)
			number++
        ```
		- enquanto a condição for verdade, o loop continua
---
- FUNÇÕES
	- criada a partir do <code>def</code>
	- váriaveis criadas dentro de função são locais
	- parametros padrão são declarados <code>nome = Visitante</code>.
	- sempre pesquise as funções built-in

---
- FUNÇÕES BUILT-IN
	- <code>len( )</code> : usado para contar o tamanho da str</li>
	- <code>range( )</code> : gera sequencia de numero</li>
	- <code>continue</code> : segue pro próximo loop sem executar o que está abaixo </li>
---
- FUNÇÕES RECURSIVAS
	- Funções que chama a si mesmo repetidamente até atingir uma condição de parada
		```python
		def fatorial(n):
			if n == 0:
				return 1
			return n * fatorial(n - 1)

		print (fatorial(5)) # saida: 120
		```
---
- FUNÇÕES ANÔNIMAS (lambda)
	- É um tipo com possibilidade de vários argumentos e uma ÚNICA expressão
		```python
		# sintaxe
		# lambda argumentos : expressão

		soma = lambda a, b : a + b
		print(soma(5,3)) # resultdado deve ser 8
		```
---
- FUNÇÕES DENTRO DE FUNÇÕES (CLOSURE)
	- São funções encapsuladas dentro de outras, são úteis para criar ter variáveis permanentes mas sem serem globais
		```python
			def multiplicar(y):
				def calcular(x):
					return x * y
			return calcular

			dobro = multiplicar(2)
			triiplo = multiplicar(3)

			print(f"O dobro de 4 é {dobro(4)}")
			print(f"O triplo de 4 é {triplo(4)}")
		```
---

