import json
import streamlit as st

def find_disease_definition(data, search_disease):
    definitions = {}
    for graph in data.get('graphs', []):
        for node in graph.get('nodes', []):
            if 'lbl' in node and node['lbl'].lower() == search_disease.lower():
                if 'meta' in node and 'definition' in node['meta']:
                    definitions[node['lbl']] = node['meta']['definition']['val']
                    return definitions  # Stop after first exact match
    return definitions

def process_file(file_path, search_disease):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return find_disease_definition(data, search_disease)

# Streamlit UI
st.title("Disease Definition Finder")
search_disease = st.text_input("Enter the disease name:")

if search_disease:
    file_path = 'hp.json'  # Make sure this file is in the same directory
    try:
        results = process_file(file_path, search_disease)
        if not results:
            st.warning("No disease definition found.")
        else:
            for lbl, definition in results.items():
                st.markdown(f"### {lbl}")
                st.write(definition)
    except FileNotFoundError:
        st.error(f"File not found: {file_path}")
    except json.JSONDecodeError:
        st.error("Error decoding JSON file.")

