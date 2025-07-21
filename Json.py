import json
import csv

with open('csv-Json.csv', 'r', encoding='utf-8') as csv_file:
    reader = csv_file.read()

def csv_to_json(reader, delimiter=',', row_separator='\n'):
    rows = reader.strip().split(row_separator)
    
    headers = rows[0].split(delimiter)
    
    result = []
    for row in rows[1:]:
        values = row.split(delimiter)
        rows_dict = {header: value for header, value in zip(headers, values)}
        result.append(rows_dict)
    
    return json.dumps(result, indent=4)

output = csv_to_json(reader)
print(output)


