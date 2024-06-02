import json
import csv

class Automato:

    def __init__(self, estado_inicial, estado_final, transicoes):
        self.estado_inicial = estado_inicial
        self.transicoes = transicoes
        self.estado_final = set(estado_final)

    def executar(self, entrada):
        estado = self.estado_inicial

        for simbolo in entrada:
            estado = self.transicoes.get((estado, simbolo), -1)
            if estado == -1:
                return False
        return estado in self.estado_final

def maquina_automato(arquivo_json):

    with open(arquivo_json, 'r') as arquivo:
        descricao = json.load(arquivo)
        estado_inicial = descricao['initial']
        estado_final = descricao['final']
        transicoes = {(int(t['from']), t['read']): int(t['to']) for t in descricao['transitions']}

    return Automato(estado_inicial, estado_final, transicoes)

def verificar_automato(automato, csv_entrada, csv_saida):
    resultado = []

    with open(csv_entrada, newline='') as csvfile:
        leitor = csv.reader(csvfile, delimiter=';')

        for linha in leitor:
            entrada_str = linha[0]
            resultado_execucao = automato.executar(entrada_str)
            resultado_str = '1' if resultado_execucao else '0'
            resultado.append([entrada_str, linha[1], resultado_str])
    
    with open(csv_saida, 'w', newline='') as csvfile:
        escritor = csv.writer(csvfile, delimiter=';')
        escritor.writerows(resultado)

def main():
    automato = maquina_automato('ex.aut.json')
    verificar_automato(automato, 'ex1_input.in.csv', 'ex1.out.csv')

main()
