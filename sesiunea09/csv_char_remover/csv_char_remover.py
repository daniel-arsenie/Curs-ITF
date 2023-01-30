import csv


# Sa se scrie o functie care citeste date dintr-un fisier csv
# si le elimina pe cele care in oricare coloana contin litera ‘a’.
# Dupa aceea va actualiza fisierul cu datele ce raman.

def remove_element_in_csv_file(target_file_name, result_file_name, char_to_search):
    with open(target_file_name, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    with open(result_file_name, 'w', newline='') as f:
        new_data = []
        for line in data:
            current_list = []
            for element in line:
                if char_to_search not in element:
                    current_list.append(element)
            new_data.append(current_list)
        writer = csv.writer(f)
        writer.writerows(new_data)


remove_element_in_csv_file("target_file.csv", 'result_file.csv', "a")
