from functools import reduce

personagens_percy = [
        { "nome": "Percy Jackson", 
          "chale": 3, 
          "pai": "Poseidon" },

        { "nome": "Annabeth Chase", 
          "chale": 6, "pai": 
          "Atena" },

        { "nome": "Grover Underwood",  
          "chale": "Sátiro", 
          "pai": "Natureza" },

        { "nome": "Luke Castellan", 
          "chale": 11, 
          "pai": "Hermes" },

        { "nome": "Thalia Grace", 
          "chale": 1, 
          "pai": "Zeus" },

        { "nome": "Clarisse La Rue", 
          "chale": 5, 
          "pai": "Ares" }
    ]

personagens_hp = [
        { "nome": "Harry Potter", 
          "casa": "Grifinória", 
          "papel": "O Escolhido" },

        { "nome": "Hermione Granger", 
          "casa": "Grifinória", 
          "papel": "Estudante brilhante" },

        { "nome": "Ron Weasley", 
          "casa": "Grifinória", 
          "papel": "Melhor amigo de Harry" },

        { "nome": "Draco Malfoy", 
          "casa": "Sonserina", 
          "papel": "Inimigo de Harry" },

        { "nome": "Luna Lovegood", 
          "casa": "Corvinal", 
          "papel": "Excêntrica e leal" },

        { "nome": "Cedrico Diggory", 
          "casa": "Lufa-Lufa", 
          "papel": "Campeão do Torneio Tribruxo" }
    ]

# Função 1: Usando map para exibir os nomes e chalés dos personagens
def usandoMap(personagens):
    nome_chale = list(map(lambda e: f"{e['nome']}, Chalé {e['chale']}", personagens))
    return nome_chale

# Função 2: Usando filter para filtrar personagens da casa Grifinória
def usandoFilter(personagens):
    casa_grif = list(filter(lambda e: e["casa"] == "Grifinória", personagens))
    return casa_grif

# Função 3: Usando reduce para calcular a média dos chalés
def usandoReduce(personagens):
    # Extraindo o número do chalé usando compreensão de lista e verificando se é um número
    chales = [int(p['chale']) for p in personagens if isinstance(p['chale'], int)]
    
    soma_total, total_chales = reduce(
        lambda acc, chale: (acc[0] + chale, acc[1] + 1),  # Acumulando soma e contagem
        chales,
        (0, 0)  # Valor inicial para soma e contagem
    )

    media = soma_total / total_chales if total_chales > 0 else 0
    return media

def main():
    # Chamando e exibindo o resultado das funções com os dados de Percy Jackson e Harry Potter
    print("Resultado usando map (Percy Jackson):")
    print(usandoMap(personagens_percy))
    print("\nResultado usando filter (Harry Potter):")
    print(usandoFilter(personagens_hp))
    print("\nResultado usando reduce (Percy Jackson):")
    print(usandoReduce(personagens_percy))

if __name__ == "__main__":
    main()
