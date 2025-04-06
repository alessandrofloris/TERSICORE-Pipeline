import json
import re
from collections import defaultdict

def save_results_as_json(out_raw_prompt, out_prompt, output_raw, output, output_path):
    '''
        Save the results as a JSON file.

        Args:
            out_raw_prompt (str): Prompt for LLaVA.
            out_prompt (str): Prompt for Gemini.
            output_raw (str): Persons information.
            output (dict): Persons information formatted.
            output_path (str): Path to save the JSON file.
    '''

    data = {
        "llava_prompt": out_raw_prompt,
        "gemini_prompt": out_prompt,
        "output_raw": output_raw,
        "output": output
    }

    with open(output_path, "w") as file:
        json.dump(data, file, indent=4)

def extract_info(img_id, individuals_info_str):
    ''' 
        Extract individuals information from a given string
    '''

    id_img = 0
    n_individuals = 0
    counter = defaultdict(int)

    # Estrazione del numero di individui
    n_individuals_match = re.search(r'\((\d+),', individuals_info_str)
    n_individuals = int(n_individuals_match.group(1)) if n_individuals_match else None

    # Estrazione della stringa che contiene le tuple
    individuals_data_match = re.search(r'\[(.*)\]', individuals_info_str)
    individuals_data_string = individuals_data_match.group(1) if individuals_data_match else None

    if individuals_data_string:
        individual_tuples = re.findall(r'\((\d+),\s*\'(.*?)\',\s*\'(.*?)\',\s*\'(.*?)\'\)', individuals_data_string)
        for individual_tuple in individual_tuples:
            _, bodily_posture, activity_level, social_configuration, age, sex = individual_tuple

            counter[bodily_posture] += 1
            counter[activity_level] += 1
            counter[social_configuration] += 1
            counter[age] += 1
            counter[sex] += 1
            
    # Stampa del risultato finale
    print(f'Risultato: {img_id} {n_individuals} {counter}')

    return id_img, n_individuals, counter