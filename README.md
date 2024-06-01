# Autômato finito determinístico

## Descrição
 
* Implementação em python de ferramenta que simula o funcionamento de um autômato finito.
* O programa lê a definição de um autômato de um JSON, executa testes em entradas de um CSV e escreve os resultados de aceitação ou rejeição em outro CSV.

## Funções do código

* **Executar**: função da classe Automato que recebe a entrada (palavra), e compara os símbolos com as especificações.

* **Maquina_automato**: recebe o arquivo JSON, e após lê-lo e converter as strings numéricas para inteiro, retorna os valores em uma instância da classe Automato.

* **Verificar_automato**: testa entradas do arquivo_CSV usando o autômato e salva os resultados em outro CSV. Ela executa cada entrada e registra se foi aceita ('1') ou não ('0').


