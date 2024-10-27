# Simulação de Máquina de Turing

Trabalho apresentado à disciplina de Teoria da Computação que diz respeito à implementação da Máquina de Turing.

## Máquina de Turing

A Máquina de Turing é um modelo universal de computação capaz de resolver qualquer problema computacional. De acordo com a hipótese de Church-Turing, ela é um dos modelos mais poderosos para descrever a computação. Essa máquina teórica foi proposta por Alan Turing em 1936 e serve como uma base para o entendimento da computabilidade e da complexidade de algoritmos.

### Estrutura

Uma Máquina de Turing é composta por três componentes principais:

1. `Fita:` A fita é uma sequência "infinita" de células, cada uma contendo um símbolo de um alfabeto finito (ex: `a`, `b`, e um símbolo em branco `_`).

2. `Gravação:` A máquina possui uma cabeça que pode mover-se para a esquerda ou para a direita na fita. A cabeça é responsável por ler o símbolo atual e escrever novos símbolos na fita.

3. `Estado:` A Máquina de Turing opera em um de um conjunto finito de estados. O estado inicial é onde a máquina começa, e ela pode transitar para outros estados conforme a execução do algoritmo.
---
### Funcionamento

As instruções com as quais a Máquina irá operar estão em um arquivo `JSON` com a seguinte estrutura:

```json
{
    "initial": 0,
    "final": [4],
    "white": "_",
    "transitions": [
        {"from": 0, "to": 1, "read": "a", "write": "A", "dir": "R"},
        {"from": 1, "to": 1, "read": "a", "write": "a", "dir": "R"},
        {"from": 1, "to": 1, "read": "B", "write": "B", "dir": "R"},
        {"from": 1, "to": 2, "read": "b", "write": "B", "dir": "L"},
        //...
    ]
}
```
Componentes das instruções:
* `initial:`o estado inicial da máquina.
* `final:` lista de estados finais.
* `white:` símbolo branco que é representado pelo caractere `_` .
* `transitions:` conjunto de "regras" que definem o comportamento da máquina.
---
Essas instruções serão utilizadas para ler a palavra contida em uma arquivo.txt:

```python
aaabbb
```
A saída esperada é:

```python
AAABBB_
```
