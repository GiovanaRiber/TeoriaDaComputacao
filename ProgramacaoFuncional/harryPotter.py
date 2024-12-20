from functools import reduce

# lista de personagens de Harry Potter
# cada personagem é um dicionário contendo informações básicas
personagens_hp = [
    { "nome": "Harry Potter", 
      "casa": "Grifinória", 
      "idade": 17 },

    { "nome": "Hermione Granger", 
      "casa": "Grifinória", 
      "idade": 17 },

    { "nome": "Ron Weasley", 
      "casa": "Grifinória", 
      "idade": 17 },

    { "nome": "Draco Malfoy", 
      "casa": "Sonserina", 
      "idade": 17 },

    { "nome": "Luna Lovegood", 
      "casa": "Corvinal", 
      "idade": 17 },

    { "nome": "Cedrico Diggory", 
      "casa": "Lufa-Lufa", 
      "idade": 18 },

    { "nome": "Neville Longbottom", 
      "casa": "Grifinória", 
      "idade": 17 },

    { "nome": "Ginny Weasley", 
      "casa": "Grifinória", 
      "idade": 16 }
]

# Função 1: número de personagens por casa
# usando a função "reduce" para acumular o número de personagens em cada casa
# a cada iteração, o "acc" é atualizado com a contagem da casa do personagem atual
def personagens_por_casa(personagens):
    return reduce(
        lambda acc, p: acc.update({p['casa']: acc.get(p['casa'], 0) + 1}) or acc,  # atualiza o contador por casa
        personagens,  # itera sobre a lista de personagens
        {}  # inicia o acumulador como um dicionário vazio
    )

# Função 2: média de idade dos personagens
# a função "sum" e "map" são usadas para calcular a soma das idades dos personagens
# após isso, dividi-se pelo número total de personagens para calcular a média
def media_idade(personagens):
    soma_idades = sum(map(lambda p: p['idade'], personagens))  # calcula a soma das idades
    total_personagens = len(personagens)  # total de personagens
    media = soma_idades / total_personagens if total_personagens > 0 else 0  # calcula a média
    return media

# Função 3: contar personagens da casa Grifinória
# a função "filter" é usada para filtrar todos os personagens que são da casa Grifinória
# depois, contamos quantos elementos estão na lista filtrada
def contar_grifinoria(personagens):
    grifinoria = filter(lambda p: p['casa'] == "Grifinória", personagens)  # filtra os personagens da Grifinória
    return len(list(grifinoria))  # conta quantos personagens

def main():

    # resultados das funções
    print("Número de personagens por casa:", personagens_por_casa(personagens_hp))
    print("Média de idade dos personagens:", media_idade(personagens_hp))
    print("Quantidade de personagens da casa Grifinória:", contar_grifinoria(personagens_hp))

if __name__ == "__main__":
    main()