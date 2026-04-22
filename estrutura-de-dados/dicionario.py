from pprint import pprint #importa a função pprint para imprimir o dicionário de forma mais legível

meu_dicionario= { "nome":"Joao" ,                                   #cria um dicionário com as chaves "nome", "sobrenome", "idade", "peso" e "filhos" e seus respectivos valores
                  "sobrenome": "Santos" ,
                    "idade":30,
                      "peso": 80.5,
                        "filhos": ["Maria","Josefina", "Pedro"]}
meu_dicionario["sobrenome"] = "Souza" #altera o valor associado à chave "sobrenome" para "Souza"
meu_dicionario['cidade'] = "Americana" #adiciona a chave "cidade" com o valor "Americana"


pprint(meu_dicionario) #imprime o dicionário usando a função pprint para uma melhor formatação





# print(meu_dicionario["nome"])             #imprime o valor associado à chave (no caso "nome") do dicionário
# print(meu_dicionario["sobrenome"])
# print(meu_dicionario["idade"])
# print(meu_dicionario["peso"]
# print(meu_dicionario["filhos"])
