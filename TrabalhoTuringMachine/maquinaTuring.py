import json

def simulacao(instrucoes_arquivo, entrada_arquivo, saida_arquivo):

    with open(instrucoes_arquivo, 'r') as instrucoes_file:
        informacoes = json.load(instrucoes_file)  # armazena as informações contidas do arquivo json

    estado_atual = informacoes['initial']      # estado inicial definido nas instruções
    estados_finais = set(informacoes['final']) # lista de estados finais
    simbolo_branco = informacoes['white']      # símbolo branco = _
    transicoes = informacoes['transitions']    # armazena as transições
    
    dicionario_transicoes = {(t['from'], t['read']): t for t in transicoes}  # adiciona as transições em um dicionário para facilitar a leitura

    with open(entrada_arquivo, 'r') as entrada_file:
        fita = list(entrada_file.read().strip())  # lê a entrada contendo a palavra e a insere em uma lista que representa a fita

    posicao = 0  # variável de controle da fita

    while estado_atual not in estados_finais:
       
        simbolo_lido = fita[posicao] if posicao < len(fita) else simbolo_branco

        chave = (estado_atual, simbolo_lido) # chave para verificar se há uma transição correspondente para o estado atual e o símbolo lido
        
        if chave not in dicionario_transicoes:  # caso uma transição ñ esteja no dicionário, o loop é finalizado
            print("Invalido") 
            break

        transicao = dicionario_transicoes[chave]

        if posicao < len(fita):
            fita[posicao] = transicao['write'] # escreve o símbolo definido na transição
        else:
            fita.append(transicao['write'])    # adiciona o símbolo na fita se estiver além do comprimento

        estado_atual = transicao['to']         # atualiza o estado atual com o novo estado definido na transição
 
        if transicao['dir'] == 'R':
            posicao += 1                   # move para a direita
        elif transicao['dir'] == 'L':
            posicao = max(0, posicao - 1)  # move para a esquerda, impedindo que a posição seja negativa

    else:
        resultado = f"{''.join(fita)}\n" # se o estado for final, junta a fita em uma string para o resultado

    with open(saida_arquivo, 'w') as saida_file:
        saida_file.write(resultado)  # grava a fita no arquivo de saída

def main():
    
    instrucoes_arquivo = "arquivo.json"
    entrada_arquivo = "entrada_1.txt"
    saida_arquivo = "saida.txt"
    
    simulacao(instrucoes_arquivo, entrada_arquivo, saida_arquivo)

if __name__ == "__main__":
    main()