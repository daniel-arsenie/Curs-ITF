import json


# Sa se scrie o functie care citeste date dintr-un fisier json
# si le imparte in alte doua fisiere astfel incat prima jumatate a datelor
# va fi in fisierul prima_jumatate.json, iar a doua in a_doua_jumatate.json.


def split_json(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f)
    jumatate = len(data) // 2
    with open('prima_jumatate.json', 'w') as f:
        json.dump(data[:jumatate], f)
    with open('a_doua_jumatate.json', 'w') as f:
        json.dump(data[jumatate:], f)


split_json('employees.json')
