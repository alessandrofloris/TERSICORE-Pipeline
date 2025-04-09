import json
import re
import os
import csv
from collections import defaultdict

def extract_info(img_id, individuals_info_str):
    ''' 
        Extract individuals information from a given string
    '''
    n_individuals = 0
    counter = defaultdict(int)

    # Estrazione del numero di individui
    n_individuals_match = re.search(r'\((\d+),', individuals_info_str)
    n_individuals = int(n_individuals_match.group(1)) if n_individuals_match else 0

    # Estrazione della stringa che contiene le tuple
    individuals_data_match = re.search(r'\[\s*([\s\S]*?)\s*\]', individuals_info_str)
    individuals_data_string = individuals_data_match.group(1) if individuals_data_match else ""
    
    individuals_data_string = individuals_data_string.strip('()')
    tuples_strings = individuals_data_string.split("), (")

    for tuple_string in tuples_strings: 
        try:
        
            #tuple_values = eval("(" + tuple_string + ")")
            #print(tuple_values)
            _, bodily_posture, activity_level, social_configuration, age, sex = tuple_string.split(", ")

            counter[bodily_posture] += 1
            counter[activity_level] += 1
            counter[social_configuration] += 1
            counter[age] += 1
            counter[sex] += 1
        except Exception as e:
            print("Error: ", e)
            continue
    
    return img_id, n_individuals, counter

def create_csv(results, universal_keys, filename="output.csv"):
    """
    Crea un file CSV con i risultati ottenuti da tutti i file JSON analizzati.

    Args:
        results (list): Lista di tuple (id_img, n_individuals, counter)
        universal_keys (list): Lista di tutte le chiavi possibili per le colonne
        filename (str): Nome del file CSV di output
    """
    header = ["Id", "N individuals"] + universal_keys
    
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        
        for id_img, n_individuals, counter in results:
            counter["NEI Age"] = n_individuals - (counter.get("Child", 0) + counter.get("Adult", 0) + counter.get("Senior", 0))
            counter["NEI Sex"] = n_individuals - (counter.get("Male", 0) + counter.get("Female", 0))
            counter["NEI Bodily Posture"] = n_individuals - (counter.get("Upright", 0) + counter.get("Seated", 0) + counter.get("Recumbent", 0))
            counter["NEI Activity Level"] =  n_individuals - (counter.get("Sedentary", 0) + counter.get("Moderate", 0) + counter.get("Vigorous", 0))
            counter["NEI Social Configuration"] =  n_individuals - (counter.get("Solitary", 0) + counter.get("Dyadic", 0) + counter.get("Group", 0))

            data = [id_img, n_individuals] + [counter.get(key, 0) for key in universal_keys]
            writer.writerow(data)

if __name__ == "__main__":
    directory = "results/"
    results = []
    universal_keys = ["Child", "Adult", "Senior", "NEI Age", "Male", "Female", "NEI Sex", "Upright", "Seated", "Recumbent", "NEI Bodily Posture", "Sedentary", "Moderate", "Vigorous", "NEI Activity Level", "Solitary", "Dyadic", "Group", "NEI Social Configuration"]

    for i in range(1, 26):
        file_path = os.path.join(directory, f"{i}_results.json")
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                data = json.load(file)
                output = data.get("gpt_output", "")
                id_img, n_individuals, counter = extract_info(i, output)
                results.append((id_img, n_individuals, counter))
    
    create_csv(results, universal_keys, "counts-modello.csv")
