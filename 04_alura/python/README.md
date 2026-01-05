<p><em>PT Este documento é um resumo feito durante o curso de 'Python: Crie seu primeiro app'. São notas pessoais.</em></p>
<p><em>EN This document is a summary made during the 'Python: Build your first app' course. These are personal notes.</em></p>

<h1>Python</h1>
<h2>Notas</h2>

<ul>
    CASE PATTERNS
    <li>'snakecase': variaveis, funcoes e métodos</li>
    <li>'PascalCase': classes</li>
    <li>'SCREAMING_CASE': constantes</li>
</ul>

<ul>
    ASPAS
    <li>Pode se usar as simples ' ', duplas " ", e triplas """ """</li>
    <li>A tripla envia tudo que estiver dentro, até quebra de linha.</li>
</ul>

<ul>
    INTERPOLAÇÃO VARIÁVEIS
    <li>f-string : <code>print(f"I'm {age} years old.")</code></li>
    <li>.format : <code>print("I'm {} years old.".format(age))</code></li>
    <li>% string antiga : <code>print("I'm %i years old."%(age))</code></li>
</ul>

<ul>
    FORMATAÇÃO PRINT
    <li><code>sep='\n'</code> : sep determina a separação no print</li>
    <ul><li><code>print('A','L','U','R','A',sep='\n')</code></li></ul>
    <li><code>end=""</code> : end determina o final do print</li>
    <ul><li><code>print("O início do termianl deve começar na mesma linha ->", end="")</code>$</li></ul>
    
</ul>

<ul>
    FORMATAÇÃO NUMEROS
    <li>f-string : pode ser usado para formatar numeral</li>
    <ul><li><code>print(f'O valor arredondado de pi é: {pi:.2f}')</code></li></ul>
    <li>.format : outra opção de formatação</li>
    <ul><li><code>print('O valor arredondado de pi é: {:.2f}'.format(pi))</code></li></ul>
    <li>round : pode ser outra opção</li>
    <ul><li>print('O valor arredondado de pi é:', round(pi, 2))</li></ul>
</ul>

<ul>
    INT STR
    <li>Lembrar de converter o formato ao usar <code>input()</code></li>
    <ul><li><code>int(input("Digite sua idade: "))</code></li></ul>
    <li>Use <code>print(type())</code> sempre que precisar identificar</li>
</ul>

<ul>
    BIBLIOTECAS
    <li>Usar <code>import</code> para isso no início do código</li>
    <li>Existem diversas bibliotecas uteis como 'os', 'math'</li>
</ul>