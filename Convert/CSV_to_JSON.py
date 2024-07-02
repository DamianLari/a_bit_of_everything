import csv
import json

def csv_to_json(csv_file, json_file):
    with open(csv_file, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
    
    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

# Exemple d'utilisation
csv_file = "Input/InputFile.csv"
json_file = "Output/OutputFile.json"
csv_to_json(csv_file, json_file)