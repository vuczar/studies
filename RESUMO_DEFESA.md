# Resumo de Defesa — A-Maze-ing (vimauric)

> Roteiro baseado na **scale oficial** (`iv/Scale_A-Maze-ing.html`), item por item.
> Para cada item: o que o avaliador verifica, como demonstrar, **onde está no código** e
> **quem fez**. No fim, um FAQ do mais simples ao mais complexo.
>
> Legenda: ⭐ = **parte minha** (vimauric) · 🟦 = parte da dilferre · 🤝 = dos dois.
>
> Tudo neste documento foi **verificado em 2026-10-29** num `git clone` limpo do `main`
> (`1f47244`): lint limpo, todos os erros testados, analisador OK nos dois modos, seed
> reproduzível, pacote reconstruído e testado em outro venv.

---

## 0. Antes de começar (preparação)

A scale manda o avaliador fazer `git clone` **numa pasta vazia** e avaliar **só o que está
no repositório**. Ensaie exatamente assim:

```bash
git clone <repo> teste && cd teste
make install          # cria venv/ e instala flake8, mypy, pytest, build
make lint             # flake8 + mypy com as flags do subject
make run              # python3 a_maze_ing.py config.txt
```

**Duas regras da scale que dão nota 0:**
- O programa **terminar de forma inesperada** (crash / traceback) → flag *Crash*.
- **Não saber explicar o código** → flag *Can't support / explain code*. Vale para o código
  dos **dois**: posso ser perguntado sobre o gerador da dilferre.

---

## 1. Basics — Submitted files and Norm

**O avaliador verifica:** `README.md`, `LICENSE.md`, `a_maze_ing.py`, `mazegen-*.whl`,
um arquivo de config, o necessário para reconstruir o pacote, e **flake8 + mypy** passando.

| Exigido | No repositório | Quem |
|---|---|---|
| `README.md` | [README.md](../../../a-maze-ing/README.md) | ⭐ |
| `LICENSE.md` (MIT) | [LICENSE.md](../../../a-maze-ing/LICENSE.md) | 🟦 |
| `a_maze_ing.py` | [a_maze_ing.py](../../../a-maze-ing/a_maze_ing.py) | ⭐ (+ `run_graphical` 🟦) |
| `mazegen-*.whl` | `mazegen-1.0.0-py3-none-any.whl` na raiz | ⭐ |
| Arquivo de config | [config.txt](../../../a-maze-ing/config.txt) | ⭐ |
| Build do pacote | [pyproject.toml](../../../a-maze-ing/pyproject.toml) + `mazegen/` | ⭐ |
| flake8 + mypy | `make lint` → [Makefile:46](../../../a-maze-ing/Makefile#L46) | 🤝 (flags obrigatórias ⭐) |

**Demonstrar:** `ls` + `make lint` → `Success: no issues found in 11 source files`.

**O que dizer:** "O `make lint` roda o `flake8 .` e o `mypy .` com as 5 flags do subject
(`--warn-return-any --warn-unused-ignores --ignore-missing-imports
--disallow-untyped-defs --check-untyped-defs`). Também temos o `make lint-strict`
com `--strict`, que passa limpo."

---

## 2. Basics — README.md ⭐

**O avaliador verifica** cada um destes itens (se faltar um, a nota é 0):

| Exigência | Onde no README |
|---|---|
| 1ª linha em itálico: *This project has been created as part of the 42 curriculum by dilferre, vimauric.* | linha 1 |
| Description | [§ Description](../../../a-maze-ing/README.md#L5) |
| Instructions | [§ Instructions](../../../a-maze-ing/README.md#L24) |
| Resources + uso de IA | [§ Resources](../../../a-maze-ing/README.md#L310), [§ How AI was used](../../../a-maze-ing/README.md#L325) |
| Descrição completa do config | [§ Configuration file](../../../a-maze-ing/README.md#L100) |
| Algoritmo escolhido | [§ Maze generation algorithm](../../../a-maze-ing/README.md#L153) |
| Porque esse algoritmo | [§ Why this algorithm](../../../a-maze-ing/README.md#L180) |
| Documentação do módulo reutilizável | [§ Reusable module](../../../a-maze-ing/README.md#L191) |
| Papéis | [§ Roles](../../../a-maze-ing/README.md#L251) |
| Planejamento e evolução | [§ Planning](../../../a-maze-ing/README.md#L258) |
| O que funcionou / melhorar | [§ What worked well](../../../a-maze-ing/README.md#L275) |
| Ferramentas | [§ Tools](../../../a-maze-ing/README.md#L300) |

**O que dizer:** "Escrevi o README seguindo a lista da scale, uma seção por exigência."

---

## 3. Standard usage — Display ⭐

**O avaliador verifica:** roda `a_maze_ing.py` com o config padrão → um labirinto aparece
(no terminal ou numa janela) e dá para interagir com ele.

**Demonstrar:** `make run`.

**Código:**
- [a_maze_ing.py:103 `main`](../../../a-maze-ing/a_maze_ing.py#L103): lê o config e decide
  entre a janela e o terminal. ⭐
- [a_maze_ing.py:41 `run_graphical`](../../../a-maze-ing/a_maze_ing.py#L41): abre a janela MLX
  **só se** houver `DISPLAY` **e** o `mlx` estiver instalado. Senão, o programa usa o terminal. 🟦
- [renderer_ascii.py:40 `render`](../../../a-maze-ing/mazegen/renderer_ascii.py#L40):
  desenha o labirinto em texto. ⭐

**Atenção:** o `config.txt` tem `SEED=42`, por isso o labirinto sai **sempre igual**. Se o
avaliador quiser ver aleatoriedade: apague a linha `SEED` **ou** use o menu `1`.

---

## 4. Standard usage — Interactive menu ⭐

**O avaliador verifica:** re-gerar, mostrar/ocultar o caminho mais curto e mudar a cor das
paredes. Interações extra são permitidas.

| Opção | O que faz | Código |
|---|---|---|
| `1` | Seed nova → gera de novo → reescreve o `maze.txt` | [a_maze_ing.py:92-94](../../../a-maze-ing/a_maze_ing.py#L92-L94) |
| `2` | `show_path = not show_path` | [a_maze_ing.py:95-96](../../../a-maze-ing/a_maze_ing.py#L95-L96) |
| `3` | `color_index = (color_index + 1) % len(WALL_COLORS)` (5 cores) | [a_maze_ing.py:97-98](../../../a-maze-ing/a_maze_ing.py#L97-L98) |
| `4` / Ctrl+D | Sai sem erro | [a_maze_ing.py:87-88](../../../a-maze-ing/a_maze_ing.py#L87-L88), [99-100](../../../a-maze-ing/a_maze_ing.py#L99-L100) |

Tudo isto está em [`interact`, a_maze_ing.py:70](../../../a-maze-ing/a_maze_ing.py#L70) ⭐.
As cores vêm de [`WALL_COLORS`, renderer_ascii.py:11](../../../a-maze-ing/mazegen/renderer_ascii.py#L11) ⭐.

Na janela MLX 🟦 as teclas são `1/R`, `2/P`, `3/C`, `T` (cor do "42") e `4/Q/Esc`.

---

## 5. Configuration file — Format ⭐🟦

**O avaliador verifica:** comentários com `#`, linhas `KEY=VALUE` (minúsculas também valem)
e as 6 chaves obrigatórias.

**Código:** [`parse_config`, config.py:89](../../../a-maze-ing/mazegen/config.py#L89). O parser
foi feito pela dilferre 🟦; eu fiz a validação e as mensagens de erro ⭐.
- Ignora linhas vazias e linhas que começam com `#`.
- Separa no **primeiro** `=` e converte a chave com `.upper()` → `width=20` funciona.
- Confere as 6 chaves obrigatórias: `WIDTH, HEIGHT, ENTRY, EXIT, OUTPUT_FILE, PERFECT`.
- Chaves opcionais: `SEED` e `ALGORITHM` (esta é lida mas não usada; só existe o backtracker).

---

## 6. Configuration file — Error Management ⭐ (a mais importante para mim)

**O avaliador edita o config** para provocar erros. **Um crash dá nota 0.** Testado, com as
mensagens exatas:

| Teste da scale | Exemplo | Mensagem do programa | Onde |
|---|---|---|---|
| Remover chave obrigatória | sem `HEIGHT` | `Error: Missing required configuration keys: HEIGHT.` | [config.py:107](../../../a-maze-ing/mazegen/config.py#L107) |
| Linha sem `=` | `WIDTH 20` | `Error: Line 7: invalid config: 'WIDTH 20'.` | [config.py:99](../../../a-maze-ing/mazegen/config.py#L99) |
| Letras no lugar de números | `WIDTH=abc` | `Error: WIDTH must be an integer, got 'abc'.` | [`parse_int`, config.py:56](../../../a-maze-ing/mazegen/config.py#L56) |
| Booleano inválido | `PERFECT=maybe` | `Error: PERFECT must be True or False, got 'maybe'.` | [`parse_bool`, config.py:65](../../../a-maze-ing/mazegen/config.py#L65) |
| Tupla mal formatada | `ENTRY=0;0` | `Error: ENTRY must be two integers 'x,y', got '0;0'.` | [`parse_tuple`, config.py:76](../../../a-maze-ing/mazegen/config.py#L76) |
| Dimensão negativa | `WIDTH=-5` | `Error: WIDTH must be greater than 0, got -5.` | [`validate_config`, config.py:21](../../../a-maze-ing/mazegen/config.py#L21) |
| Entry/exit fora | `EXIT=20,14` | `Error: EXIT 20,14 is outside the maze bounds (0,0 to 19,14).` | idem |
| Entry = exit | `EXIT=0,0` | `Error: ENTRY and EXIT must be different cells, both are 0,0.` | idem |
| Arquivo inexistente | `/nope.txt` | `Error: /nope.txt: No such file or directory.` | [`main`, a_maze_ing.py:120](../../../a-maze-ing/a_maze_ing.py#L120) |
| Pasta em vez de arquivo | `/tmp` | `Error: /tmp: Is a directory.` | idem |
| Sem argumento | — | `Usage: python3 a_maze_ing.py <config_file>` | [a_maze_ing.py:112](../../../a-maze-ing/a_maze_ing.py#L112) |

`ENTRY=(0,0)` também é aceito (os parênteses são removidos).

**Como funciona** (o que explicar):
1. Todos os erros de **conteúdo** viram `ValueError`, com uma mensagem que diz **qual campo**
   está errado (cada `parse_*` recebe o nome da chave).
2. Todos os erros de **arquivo** (não existe, é uma pasta, sem permissão) são `OSError`.
3. O [`main`](../../../a-maze-ing/a_maze_ing.py#L116-L125) captura os dois tipos de erro,
   imprime `Error: ...` e devolve o código `1`. **Nunca há traceback.**
4. `Ctrl+C` → `Interrupted.` e o código `130` ([a_maze_ing.py:129-134](../../../a-maze-ing/a_maze_ing.py#L129-L134)).

---

## 7. Output file — Format 🤝

**O avaliador verifica:** que o **primeiro** labirinto mostrado está gravado no arquivo, com
`HEIGHT` linhas de `WIDTH` caracteres, uma linha vazia, a entry, a exit e o caminho em
`N/E/S/W`. Depois roda o analisador e compara o caminho do arquivo com o desenho.

**Demonstrar:**
```bash
make run              # escolher 4 logo (o "1" reescreve o maze.txt!)
cat maze.txt
python3 maze_analyzer.py maze.txt
```

**Código:**
- [`write_output`, generator.py:232](../../../a-maze-ing/mazegen/generator.py#L232) 🟦:
  `f"{cell:X}"` grava cada célula como um dígito hex maiúsculo, dentro de um `with open(...)`.
- [`shortest_path`, generator.py:249](../../../a-maze-ing/mazegen/generator.py#L249) ⭐: a BFS
  que gera a string `"EESEN..."`.
- [`path_cells`, renderer_ascii.py:20](../../../a-maze-ing/mazegen/renderer_ascii.py#L20) ⭐:
  "anda" a **mesma string** a partir da entry para marcar os `·` no desenho. É por isso que o
  caminho do arquivo e o desenho **batem sempre**.

**Ler um dígito:** N=1, E=2, S=4, W=8, e o bit a 1 significa **parede fechada**.
Exemplo: `D` = 13 = 8+4+1 → paredes W, S e N fechadas, só o lado **E aberto**. `F` = tudo
fechado (as células do "42").

---

## 8. Maze Generator module — Maze generation 🟦 (+ BFS ⭐)

Item por item da scale:

| Exigência | Como cumprimos | Código | Quem |
|---|---|---|---|
| Aleatório com o módulo `random` | `rng = random.Random(seed)`: um gerador **próprio** | [generator.py:213](../../../a-maze-ing/mazegen/generator.py#L213) | 🟦 |
| Parâmetros inconsistentes | `validate_config` rejeita com mensagem clara (ver §6) | [config.py:21](../../../a-maze-ing/mazegen/config.py#L21) | ⭐ |
| Todas as células alcançáveis (menos o "42") | `ensure_full_connectivity` | [generator.py:308](../../../a-maze-ing/mazegen/generator.py#L308) | 🟦 |
| Paredes em toda a volta | A grade começa toda com `15`, e `remove_wall` recusa células fora da grade → a borda nunca é aberta | [generator.py:141](../../../a-maze-ing/mazegen/generator.py#L141) | 🟦 |
| **Sem zona aberta 3×3** (o avaliador **pergunta como**) | Perfeito: impossível por construção. Jogável: `_creates_open_area` | [generator.py:383](../../../a-maze-ing/mazegen/generator.py#L383) | 🟦 |
| Padrão "42" (ou mensagem se não couber) | `_apply_pattern_42`: centrado, mínimo 9×7, senão `Warning: maze too small...` | [generator.py:182](../../../a-maze-ing/mazegen/generator.py#L182) | 🟦 |
| `PERFECT=True` → perfeito | Backtracker = spanning tree → analisador: `PERFECT maze` | [generator.py:210](../../../a-maze-ing/mazegen/generator.py#L210) | 🟦 |
| `PERFECT=False` → Pac-Man | `generate_playable` → analisador: `Pac-Man-USABLE` | [generator.py:567](../../../a-maze-ing/mazegen/generator.py#L567) | 🟦 |
| Mesma seed = mesmo labirinto | Rodar duas vezes e comparar com `cmp` → idênticos | — | 🟦 |

**Resultados verificados** com o `config.txt` (15×15, seed 42):
- `PERFECT=True` → `PERFECT maze: a single path, no loop`.
- `PERFECT=False` → `Pac-Man-USABLE`: 23 loops, 2 dead-ends reais + 3 fechados pelo "42"
  (tolerados), cantos e centro alcançáveis.
- `WIDTH=5, HEIGHT=5` → `Warning: maze too small to draw the '42' pattern.`, e o labirinto
  é gerado na mesma.

**A resposta sobre o 3×3** (a scale manda perguntar):
- **Modo perfeito:** uma zona 2×2 toda aberta já forma um ciclo. Um labirinto perfeito não
  tem ciclos, logo não pode ter nem 2×2 aberto, quanto mais 3×3.
- **Modo jogável:** antes de abrir qualquer parede extra, o código **remove-a
  temporariamente, verifica todas as janelas 3×3 que contêm a célula e volta a colocá-la**.
  Só abre a parede se não formar uma zona 3×3 aberta.

**Como demonstrar a seed:**
```bash
make run   # 4
cp maze.txt a.txt
make run   # 4
cmp maze.txt a.txt && echo iguais
```

---

## 9. Maze Generator module — Reusable module ⭐

**O avaliador verifica:** que reconstruímos o pacote num venv e depois, **noutro venv**, o
instalamos e testamos com o `a_maze_ing.py` e o config.

**Demonstrar (testado):**
```bash
rm mazegen-1.0.0-py3-none-any.whl
make install && make build                       # → mazegen-1.0.0-py3-none-any.whl na raiz
python3 -m venv /tmp/v2
/tmp/v2/bin/pip install mazegen-1.0.0-py3-none-any.whl
mkdir /tmp/fora && cp a_maze_ing.py config.txt /tmp/fora && cd /tmp/fora
/tmp/v2/bin/python a_maze_ing.py config.txt
/tmp/v2/bin/python -c "import mazegen; print(mazegen.__file__)"   # → .../site-packages/mazegen
```

> ⚠️ **Rode a partir de uma pasta FORA do repositório.** O Python procura os imports primeiro
> na pasta do script. Dentro do repo ele importaria a pasta `mazegen/` local e não o pacote
> instalado, e o teste não provaria nada.

**Código:**
- [pyproject.toml](../../../a-maze-ing/pyproject.toml) ⭐: backend `setuptools`, nome
  `mazegen`, versão `1.0.0`, licença MIT, `packages = ["mazegen"]` (só a pasta `mazegen/` entra
  no pacote).
- [Makefile:35 `build`](../../../a-maze-ing/Makefile#L35) ⭐: `python -m build --wheel --outdir .`
- [mazegen/__init__.py](../../../a-maze-ing/mazegen/__init__.py) 🟦: exporta `MazeConfig`,
  `parse_config`, `MazeGenerator` e `Direction`, e traz um exemplo de uso na docstring.

---

## 10. Bonuses

**Não fizemos bônus.** A decisão foi fazer só a parte obrigatória (está no README). A janela
MLX **não é bônus**: o subject pede terminal **ou** janela, e nós temos as duas formas. Se
perguntarem, a resposta honesta é "não fizemos bônus".

---

## 11. Pontos de atenção (riscos)

1. **README, linha 277:** existe uma linha solta `- Everything 🙃` em *What worked well and
   what could be improved*. Parece brincadeira e pode passar má impressão. **Sugestão: apagar
   antes da defesa** (o README é meu).
2. **`make install-mlx`** aponta para `vendor/mlx-2.2-py3-none-any.whl`, que **não está no
   repo** → a regra falha. Não afeta a parte obrigatória (sem MLX o programa usa o terminal).
   Avisar a dilferre.
3. **O menu `1` reescreve o `maze.txt`.** Quando o avaliador for ver o arquivo do "primeiro
   labirinto", saia com `4` antes de re-gerar.
4. **O `config.txt` vem com `PERFECT=True`.** A scale chama `False` de "default". Para mostrar
   o modo jogável basta editar o config, o que a scale permite.

---

## 12. FAQ — perguntas prováveis do avaliador

### Nível 1 — Básico

**1. O que o projeto faz?**
Lê um config, gera um labirinto (perfeito ou estilo Pac-Man) com o "42" desenhado, grava-o em
hex num arquivo junto com o caminho mais curto e mostra-o com um menu interativo.

**2. Como se roda?**
`make install` e depois `make run`, ou `python3 a_maze_ing.py config.txt`.

**3. ⭐ O que você fez?**
Validação do config, BFS do caminho mais curto, `a_maze_ing.py` (fluxo, erros, menu),
renderer ASCII, `pyproject.toml` + `.whl` e o README. A dilferre fez o parser inicial, o
gerador, o "42", o modo jogável, o MLX e a LICENSE.

**4. O que é a seed?**
O número que inicializa o gerador aleatório. Com a mesma seed sai sempre o mesmo labirinto.
Sem `SEED` fica `None` e o Python usa o relógio, por isso sai um labirinto diferente a cada
execução.

**5. Qual a licença e porquê?**
MIT: curta e permissiva. Permite reutilizar e distribuir o módulo, como o subject pede.

**6. ⭐ Como a IA foi usada?**
Como consulta (conceitos, documentação de Python e de empacotamento) e para organizar as
tarefas. O código foi escrito, testado e revisto por nós, e sei explicar cada parte.

**7. O que é um grafo, e o que isso tem a ver com o labirinto?**
Vértices ligados por arestas. Cada célula é um vértice e cada parede aberta é uma aresta. Um
labirinto perfeito é uma árvore (*spanning tree*).

### Nível 2 — Intermediário (foco na minha parte)

**8. ⭐ Como o config é lido e validado?**
`parse_config` lê linha a linha, ignora `#` e linhas vazias, separa no primeiro `=`, confere
as chaves obrigatórias e converte com `parse_int`, `parse_tuple` e `parse_bool`. No fim,
`validate_config` confere as regras: dimensões > 0, entry e exit dentro da grade e diferentes,
nome do arquivo de saída não vazio.

**9. ⭐ Porque é que cada `parse_*` recebe o nome da chave?**
Para a mensagem dizer **qual** campo está errado: `WIDTH must be an integer, got 'abc'`, em vez
do `invalid literal for int()` do Python.

**10. ⭐ Porque capturar `OSError` e não só `FileNotFoundError`?**
`OSError` é a classe-mãe de todos os erros de arquivo: não existe, é uma pasta, sem
permissão, arquivo de saída que não dá para criar. Com uma só cláusula `except` cobrimos
todos.

**11. ⭐ Como garante que o programa nunca crasha?**
O `main` captura `OSError` e `ValueError`. O `__main__` captura o `KeyboardInterrupt`
(Ctrl+C). O menu trata o `EOFError` (Ctrl+D). Testei mais de 10 entradas inválidas e nenhuma
deu traceback.

**12. ⭐ E se as chaves estiverem em minúsculas?**
Funciona: a chave passa por `.upper()`. O `parse_bool` também ignora maiúsculas e minúsculas
(`true`, `True`, `yes`, `1`…).

**13. ⭐ Como funciona a BFS do caminho mais curto?**
Usa uma fila (`deque`) a partir da entry. Para cada célula, olha os 4 vizinhos e só passa se o
bit da parede for 0. Guarda `parent[vizinho] = (célula, letra)`. Quando chega à exit, volta
para trás pelos `parent`, junta as letras e inverte a string.
→ [generator.py:249](../../../a-maze-ing/mazegen/generator.py#L249)

**14. ⭐ Porque é que a BFS dá o caminho MAIS CURTO?**
Ela explora por "camadas" de distância: primeiro todas as células a 1 passo, depois as a 2, e
assim por diante. A primeira vez que chega à exit é necessariamente pelo menor número de
passos.

**15. ⭐ Porque `deque` e não uma lista?**
`popleft()` no `deque` é O(1). `list.pop(0)` é O(n), porque desloca todos os elementos.

**16. ⭐ Porque é que o caminho do arquivo bate com o desenho?**
Os dois vêm da **mesma string**. `path_cells` anda essas letras a partir da entry e devolve as
células visitadas, que o `render` marca com `·`.

**17. ⭐ Como o ASCII desenha as paredes?**
Cada linha da grade vira 2 linhas de texto: a de cima desenha a parede **Norte** de cada
célula (`+---+`) e a do meio desenha a parede **Oeste** (`|`) e o conteúdo da célula. No fim
entram a parede Este da última coluna e a parede Sul da última linha. Como as paredes são
coerentes, basta desenhar N e W de cada célula para não desenhar nada duas vezes.

**18. ⭐ Como funcionam as cores?**
Com códigos ANSI (`\033[32m` = verde, `\033[0m` = reset), sem nenhuma biblioteca.
`WALL_COLORS` tem 5 cores, e o `% len(...)` volta ao início depois da última.

**19. ⭐ O que faz o `replace(config, seed=...)` no re-gerar?**
`dataclasses.replace` cria uma **cópia** do `MazeConfig` só com a seed trocada. A seed nova
aparece no ecrã, por isso dá para reproduzir esse labirinto depois.

**20. ⭐ Como se reconstrói o pacote e o que vai dentro dele?**
`make build` roda `python -m build --wheel --outdir .`, que lê o `pyproject.toml`. Só a pasta
`mazegen/` entra no pacote (`packages = ["mazegen"]`). O `a_maze_ing.py` é o programa que
**usa** o pacote.

**21. ⭐ Como se usa o módulo noutro projeto?**
```python
from mazegen import MazeConfig, MazeGenerator
cfg = MazeConfig(width=20, height=15, entry=(0, 0), exit=(19, 14),
                 output_file="m.txt", perfect=True, seed=42)
gen = MazeGenerator(cfg)
gen.generate()
gen.grid             # a estrutura: grid[y][x] = bits das paredes
gen.shortest_path()  # a solução: "EESN..."
```

**22. Como funciona a codificação hex?**
Um bit por parede: N=1, E=2, S=4, W=8, com 1 = parede fechada. `3` = N+E fechadas. `F` = todas
fechadas.

**23. Como garantem a coerência entre vizinhos?**
`remove_wall(a, b)` limpa o bit **nas duas células** ao mesmo tempo: E em A e W em B.
→ [generator.py:141](../../../a-maze-ing/mazegen/generator.py#L141)

**24. Porque o recursive backtracker?**
É simples (uma pilha, um conjunto de visitados e uma escolha aleatória), gera um labirinto
perfeito com corredores longos e é uma boa base para o modo jogável.

### Nível 3 — Avançado (código da dilferre que também tenho de saber)

**25. Como funciona o backtracker, passo a passo?**
Começa na entry, com as células do "42" já marcadas como visitadas. Olha o topo da pilha: se
tem vizinhos não visitados, escolhe um ao acaso, abre a parede entre os dois, marca-o e
empilha-o. Se não tem, desempilha. Termina quando a pilha fica vazia.
→ [generator.py:210](../../../a-maze-ing/mazegen/generator.py#L210)

**26. Porque é iterativo e não recursivo?**
Com recursão, uma grade grande ultrapassa o limite de recursão do Python (~1000 chamadas). Com
uma pilha explícita esse limite não existe.

**27. Porque é que o resultado é perfeito?**
Cada célula é visitada uma única vez e entra na árvore por **uma** parede aberta. São N
células e N−1 passagens: é uma árvore, logo sem ciclos e com um único caminho entre duas
células.

**28. Porque é que as células do "42" ficam `F`?**
São postas em `visited` **antes** do backtracker, por isso ele nunca entra nelas e as paredes
nunca são abertas. Ficam com o valor inicial 15.

**29. Onde fica o "42" e o que acontece numa grade pequena?**
Fica centrado. O desenho ocupa 7×5 e precisa de uma grade de pelo menos 9×7. Numa grade menor
aparece `Warning: maze too small to draw the '42' pattern.` e o labirinto é gerado sem o "42".
→ [generator.py:182](../../../a-maze-ing/mazegen/generator.py#L182)

**30. O "42" pode tapar o centro, que tem de estar aberto no modo Pac-Man?**
Não. A coluna vazia entre o "4" e o "2" cai sempre numa coluna central.

**31. Como funciona o modo jogável?**
São 5 passos em [`generate_playable`](../../../a-maze-ing/mazegen/generator.py#L567):
1. Gera a base perfeita.
2. Abre os cantos e o centro.
3. Abre paredes até haver pelo menos 2 loops.
4. Reduz os dead-ends reais até sobrarem no máximo 2.
5. Faz uma verificação final de conectividade.

Nos passos 3 e 4 nenhuma parede é aberta se criar uma zona 3×3 aberta.

**32. Como contam os loops?**
Com `passagens abertas − células alcançáveis + 1`, a mesma fórmula do analisador. A condição
`(nx, ny) > (x, y)` conta cada passagem só uma vez.

**33. Para que serve `ensure_full_connectivity`? Ela cria loops no modo perfeito?**
Liga qualquer pedaço isolado à região alcançável a partir da entry. Abre **uma** parede por
pedaço, por isso não cria ciclos: o modo perfeito continua perfeito.

**34. Porque `seed + 1000` e `seed + 2000`?**
O modo jogável usa um gerador separado para os loops e outro para os dead-ends. Tudo continua
a depender só da `SEED`, por isso o resultado é reproduzível.

**35. O que é um dead-end "real" e um "enclosed"?**
Os dois são células com uma só passagem aberta. O real tem pelo menos uma parede que daria
para abrir para uma célula normal. O enclosed fica cercado pelo "42" ou pela borda, e o
analisador tolera-o.

**36. Porque é que às vezes abre uma janela e outras vezes o terminal?**
`run_graphical` só abre o MLX se houver display e o `mlx` estiver instalado. Senão, usa o
ASCII. No Mac, sem X11, é sempre o ASCII.

**37. Qual a complexidade da BFS?**
O(V + E). Numa grade cada célula tem no máximo 4 vizinhos, por isso fica O(largura × altura).

**38. E se a exit for inalcançável?**
`shortest_path` devolve `""`. Na prática não acontece: a exit nunca vira célula do "42" e o
`ensure_full_connectivity` liga todas as outras células.

---

## 13. Roteiro rápido da defesa (ordem sugerida)

1. `git clone` numa pasta vazia → `ls` (§1).
2. `make install` → `make lint` (§1).
3. Mostrar o README seção por seção (§2).
4. `make run` → menu `2`, `3`, `1`, `4` (§3, §4).
5. `cat maze.txt` + `python3 maze_analyzer.py maze.txt` (§7).
6. Editar o config → os erros da tabela da §6.
7. `PERFECT=False` → analisador → `Pac-Man-USABLE`. Grade 5×5 → warning do "42". Seed → `cmp` (§8).
8. Rebuild do pacote + venv novo + rodar fora do repo (§9).
