from itertools import combinations
from collections import defaultdict, OrderedDict

# remover vazios
def removerProducoesVazias(gramatica):
    vazias_diretas = {variavel for variavel, terminais in gramatica.items() if 'e' in terminais} # identificar variáveis que geram vazio diretamente
    
    while True: # identificar variáveis que geram vazio indiretamente
        vazias_indiretas = vazias_diretas.copy()
        vazias_indiretas.update(variavel for variavel, terminais in gramatica.items()
                    if variavel not in vazias_diretas and any(
                    all(s in vazias_diretas or s == 'e' for s in producoes) for producoes in terminais))
        if vazias_indiretas == vazias_diretas:
            break
        vazias_diretas = vazias_indiretas

    gramatica_nova = {}  # cria nova gramática 
    for variavel, terminais in gramatica.items():
        novas_producoes = set()
        for producoes in terminais:
            if producoes == 'e':  # não considera as produções que geram vazio
                continue
            indices_v = [i for i, c in enumerate(producoes) if c in vazias_diretas]
            for i in range(len(indices_v) + 1):
                novas_producoes.update(''.join(producoes[j] for j in range(len(producoes)) if j not in comb)
                                        for comb in combinations(indices_v, i))
        gramatica_nova[variavel] = list(filter(None, novas_producoes))  # remove produções vazias

    return gramatica_nova

# remover os inúteis e inalcançáveis
def removerNaoAlcancaveis(gramatica): # passo 1
    inicial = next(iter(gramatica))
    alcancaveis = set()
    lista = [inicial]

    while lista:
        variavel = lista.pop()
        if variavel not in alcancaveis:
            alcancaveis.add(variavel)
            lista.extend(s for terminais in gramatica.get(variavel, []) for s in terminais if s.isupper() and s not in alcancaveis)

    return {variaveis: [producao for producao in terminais if all(s in alcancaveis or s.islower() for s in producao)]
            for variaveis, terminais in gramatica.items() if variaveis in alcancaveis}

def removerNaoDerivaveis(gramatica): # passo 2
    derivaveis, novas_producoes = set(), {variaveis: set() for variaveis in gramatica}

    while True:
        tamanho = len(derivaveis)
        for variaveis, terminais in gramatica.items():
            for producao in terminais:
                if all(s in derivaveis or s.islower() for s in producao):
                    derivaveis.add(variaveis)
                    novas_producoes[variaveis].add(producao)
        if len(derivaveis) == tamanho:
            break

    return {variaveis: list(producao) for variaveis, producao in novas_producoes.items() if variaveis in derivaveis}

# substituir produções 
def substituirProducoes(gramatica):
    producoes_binarias = {variaveis: {terminal for terminal in terminais if len(terminal) == 1 and terminal.isupper()}
                          for variaveis, terminais in gramatica.items()}
    substituicoes = defaultdict(set)
    
    def processar(variaveis):
        lista, visitados = list(producoes_binarias[variaveis]), set()
        while lista:
            s = lista.pop()
            if s not in visitados:
                visitados.add(s)
                substituicoes[variaveis].update(gramatica.get(s, []))
                lista.extend(p for p in producoes_binarias.get(s, []) if p not in visitados)
    
    for variaveis in producoes_binarias:
        processar(variaveis)
    
    return OrderedDict((variaveis, list(set(terminais + list(substituicoes[variaveis])) - {p for p in terminais if len(p) == 1 and p.isupper()}))
                       for variaveis, terminais in gramatica.items())