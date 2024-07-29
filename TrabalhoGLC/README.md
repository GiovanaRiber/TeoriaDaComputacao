# Simplificador de Gramáticas Livres de Contexto

Trabalho apresentado à disciplina de Teoria da Computação, que aborda a implementação de algoritmos em Python para a simplificação e normalização de Gramáticas Livres de Contexto (GLCs).

## Simplificação de GLCs

Para que uma Gramática seja mais compreensível e utilizável, ela deve passar pelo processo de simplificação. Esse processo é composto por três etapas:

1. Eliminação de produções vazias : Remove produções que geram `ε`.
2. Eliminação de produções inúteis e inalcançáveis:
    * Produções inúteis: Remove variáveis que não geram terminais.
    (`S -> A`,
    `A -> B`)
    * Produções inalcançáveis: Remove variáveis que não podem ser alcançadas pelo símbolo inicial. 
    (`S -> Aa`, 
    `B -> b`)
3. Substituição de produção : Substitui produções unitárias (`A -> B`) por suas produções equivalentes.

## Funcionamento

A gramática a ser simplificada é recebida em um arquivo."txt" no formato:

```python
S -> aAa | bBv
A -> a | aA
```
Esse arquivo é lido e convertido em um dicionário **Python** para facilitar a manipulação das produções ao longo do programa.

```python
{
    'S': ['aAa', 'bBv'], 
    'A': ['a', 'aA']
}
```

No arquivo **mainSimplificacoes.py**, todas as funções necessárias para a simplificação são importadas e utilizadas. 
E elas são:

* `removerProducoesVazias`
* `removerNaoAlcancaveis`
* `removerNaoDerivaveis`
* `substituirProducoes`

### Exemplo

```python
from simplificacoes import removerProducoesVazias, removerNaoDerivaveis, removerNaoAlcancaveis, substituirProducoes

# [...]funções de ler gramática e escreve-la no arquivo[...]

def main():

    arquivo_saida = 'saida.txt'

    gramatica = lerGramatica('entrada_inicial.txt')
    print(gramatica)
    gramatica = removerProducoesVazias(gramatica)
    escreverGramatica(gramatica, arquivo_saida)

    gramatica = removerNaoAlcancaveis(gramatica)
    gramatica = removerNaoDerivaveis(gramatica)
    escreverGramatica(gramatica, arquivo_saida)

    gramatica = substituirProducoes(gramatica)
    escreverGramatica(gramatica, arquivo_saida)

if __name__ == "__main__":
    main()
```

## Normalização de GLCs

A normas formais são uma forma de padronizar e otimizar uma gramática. Existem duas formas principais de nomalização, sendo elas:

1. Norma Formal de Chomsky: Todas as produções são na forma `A -> BC` ou `A -> a`.
2. Norma Formal de Greibah: Todas as produções são na forma `A -> aα `, sendo α uma palavra de V.

### Norma Formal de Chomsky (implementação)

Para que uma Gramática Livre de Contexto se adeque a Forma Normal de Chomsky, ela precisa ter passado pelo processo de simplificação. Para que isso se concretize, no **mainSimplificacoes.py** é gerado um arquivo simplificado que será a gramática de entrada para o algoritmo CNF.

```python
S -> aAa
A -> a | aA
```
Eis as funções que manipularão a gramática:
* `criarVariavel:` cria uma nova variável 
* `criarProducao:` cria produções para as variáveis geradas pela função anterior
* `verificaTerminais:` verifica se os terminais estão de acordo as regras da norma
* `processar:` controlador das demais funções

O arquivo de saída com a gramática resultante é neste formato:

```python
Y2 -> a
Y1 -> Y2A
Y3 -> a
S -> Y1Y3
Y4 -> a
A -> Y4 | Y5A
Y5 -> a
```