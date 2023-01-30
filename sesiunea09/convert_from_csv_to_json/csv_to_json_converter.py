import csv
import json


# Sa se scrie o functie care citeste date dintr-un fisier csv
# si le scrie intr-un fisier json. Functia primeste numele fisierelor ca parametri.

def from_csv_to_json(file_name_csv, file_name_json):
    data_dict = {}
    with open(file_name_csv) as f:
        reader = csv.DictReader(f)
        for rows in reader:
            key = rows['Username']
            data_dict[key] = rows

    with open(file_name_json, 'w') as f1:
        json.dump(data_dict, f1, indent=4)


from_csv_to_json('username.csv', 'username.json')
