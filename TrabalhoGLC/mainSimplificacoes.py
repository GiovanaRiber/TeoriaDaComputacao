from simplificacoes import removerProducoesVazias, removerNaoDerivaveis, removerNaoAlcancaveis, substituirProducoes

def lerGramatica(arquivo):
    gramatica = {}
    
    with open(arquivo, 'r') as f:
        for l in f:
            l= l.strip()  # remove espaços em branco no início e no fim
            
            if '->' in l:
                variaveis, terminais = map(str.strip, l.split('->'))  # divide a linha e remove espaços
                terminais = [a.strip() for a in terminais.split('|')]  # divide os terminais e remove espaços
                gramatica.setdefault(variaveis, []).extend(terminais)  # adiciona os terminais à lista da variável
    return gramatica

def escreverGramatica(gramatica, arquivo):
    with open(arquivo, 'a') as arquivo:
       
        if arquivo.tell() > 0:  # linha em branco
            arquivo.write('\n')

        for variavel, terminais in gramatica.items():
            l = f"{variavel} -> {' | '.join(terminais)}"
            arquivo.write(l + '\n')

def main():

    arquivo_saida = 'saida_simplificacao.txt'
    arquivo_final = 'entrada_chomsky.txt'

    gramatica = lerGramatica('entrada_inicial.txt')
    print(gramatica)
    gramatica = removerProducoesVazias(gramatica)
    escreverGramatica(gramatica, arquivo_saida)

    gramatica = removerNaoAlcancaveis(gramatica)
    gramatica = removerNaoDerivaveis(gramatica)
    escreverGramatica(gramatica, arquivo_saida)

    gramatica = substituirProducoes(gramatica)
    escreverGramatica(gramatica, arquivo_saida)

    with open(arquivo_final, 'w') as arquivo:
        for variavel, terminais in gramatica.items():
            linha = f"{variavel} -> {' | '.join(terminais)}"
            arquivo.write(linha + '\n')

if __name__ == "__main__":
    main()