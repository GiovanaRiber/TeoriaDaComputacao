from collections import defaultdict
from mainSimplificacoes import lerGramatica, escreverGramatica
import string

def criarVariavel(cont):
    return f"Y{cont}"

def criarProducao(producao, cont, gramatica):
    num_var = (len(producao) - 1) // 2 # cálculo de variáveis novas necessárias
    simbolos = []
    
    for i in range(num_var):
        part = producao[:2]  # guarda os primeiros dois símbolos
        nova_variavel = criarVariavel(cont)
        cont += 1

        if nova_variavel not in gramatica: # adiciona nova variável nas produções
            gramatica[nova_variavel] = []
        gramatica[nova_variavel].append(part)
        
        simbolos.append(nova_variavel)
        producao = producao[2:]  # atualiza a produção para o restante
    
    if len(producao) > 0: # verificação adicional
        simbolos.append(producao)

    return ''.join(simbolos), cont # símbolo processado e o contador atualizado

def verificaTerminais(gramatica, cont):
    novas_producoes = defaultdict(list)

    for variavel, terminais in gramatica.items():
        for terminal in terminais:
            nova_producao = []

            for simbolo in terminal:
                if simbolo in string.ascii_lowercase: # verifica se o simbolo é minúsculo
                    nova_variavel = criarVariavel(cont)
                    cont += 1
                    novas_producoes[nova_variavel] = [simbolo]
                    nova_producao.append(nova_variavel)
                else:
                    nova_producao.append(simbolo)
            novas_producoes[variavel].append(''.join(nova_producao))
    
    return novas_producoes, cont

def processar(gramatica):
    novas_producoes = defaultdict(list)
    cont = 1
    for variavel, producoes in gramatica.items(): # processa as produções para garantir que cada produção tenha no máximo 2 símbolos
        for producao in producoes:
            nova_producao, cont = criarProducao(producao, cont, novas_producoes)
            novas_producoes[variavel].append(nova_producao)
    novas_producoes, cont = verificaTerminais(novas_producoes, cont) # substitui terminais nas produções não terminais

    return novas_producoes

def main():
    gramatica_inicial = 'entrada_chomsky.txt'
    gramatica_saida = 'saida_chomsky.txt'

    gramatica = lerGramatica(gramatica_inicial)
    gramatica = processar(gramatica)
    escreverGramatica(gramatica, gramatica_saida)

if __name__ == "__main__":
    main()