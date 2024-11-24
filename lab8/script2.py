#!/usr/bin/env python3

import json

with open('/Users/ben/json-practice-bg/lab8/schacon.repos.json', 'r') as file:
    data = json.load(file)

with open('chacon.csv', 'w') as csv_file:
    for entry in data[:5]:
        name = entry.get('name', '')
        html_url = entry.get('html_url', '')
        updated_at = entry.get('updated_at', '')
        visibility = entry.get('visibility', '')
        line = f"{name},{html_url},{updated_at},{visibility}\n"
        csv_file.write(line)

print("CSV file 'chacon.csv' has been created with 5 entries.")
