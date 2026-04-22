from pprint import pprint

meu_dicionario= { "nome":"Joao" ,
                  "sobrenome": "Santos" ,
                    "idade":30,
                      "peso": 80.5,
                        "filhos": ["Maria","Josefina", "Pedro"]}
meu_dicionario['dado_aleatorio'] = {'a':1,'b':2,'c':3} #cria uma nova chave

pprint(meu_dicionario)
pprint(meu_dicionario.keys()) #apresenta as chaves sem os valores

pprint(meu_dicionario.values()) #apresenta somente os valores

pprint(meu_dicionario.items()) #imprime o conjunto chave valor dentro do parenteses (dupla)