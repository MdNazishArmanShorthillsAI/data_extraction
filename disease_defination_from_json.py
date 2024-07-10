import json

def find_disease_definition(data, search_disease):
    definitions = {}
    found_exact_match = False
    for graph in data['graphs']:
        for node in graph['nodes']:
            if 'lbl' in node and node['lbl'].lower() == search_disease.lower():
                if 'meta' in node and 'definition' in node['meta']:
                    definitions[node['lbl']] = node['meta']['definition']['val']
                    found_exact_match = True
                    break  
        if found_exact_match:
            break
    return definitions

def process_file(file_path, search_disease):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return find_disease_definition(data, search_disease)

file_path = 'hp.json'
search_disease = input("Enter the disease to search for : ")
keys = process_file(file_path, search_disease)

if not keys:
    print("No disease definition found.")
else:
    for lbl, definition in keys.items():
        print(f"{lbl}: {definition}\n")
