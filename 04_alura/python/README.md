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

<ul>
    <li>Listas : mutável</li>
    <ul><li>Use [ ] para declarar : <code>variavel = []</code></li></ul>
    <li>Tuplas : não mutável</li>
    <ul><li>Use ( ) para declarar : <code>variavel = ()</code></li></ul>
</ul>

<ul>
    IF,ELIF,ELSE
    <li>Pode se fazer de forma estruturada ou ternário</li>
    <ul><li><code>
        if a % 2:
            print("even")
        elif a % 2 and a > 1:
            print("even with one divisor")
        else:
            print("odd")
    </code></li></ul>
    <ul><li><code>print("hot" if temperature > 30 else "not too hot" )</code></li></ul>
</ul>

<ul>
    FOR AND WHILE
    <li>For</li>
    <ul>
        <li>
            <code>for nome in nomes:
                print(nome)
            </code>
        </li>
        <li>para cada elemento dentro do iterável(nomes), a variável (nome) recebe o valor do elemento </li>
    </ul>
    <li>While</li>
    <ul>
        <li>
            <code>
                while number < 3:
                    print(number)
                    number++
            </code>
        </li>
        <li>enquanto a condição for verdade, o loop continua</li>
    </ul>
</ul>

<ul>
    FUNCOES ÚTEIS
    <li><code>len( )</code> : usado para contar o tamanho da str</li>
    <li><code>range( )</code> : gera sequencia de numero</li>
    <li><code>continue</code> :  </li>
</ul>