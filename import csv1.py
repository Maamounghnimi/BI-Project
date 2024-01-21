import csv
import json

csv_file_path = r'C:\Users\ASUS\Desktop\DBMS\final versions\Transactions_info_sorted1.csv'
json_file_path = r'C:\Users\ASUS\Desktop\DBMS\final versions\Transactions_info_sorted1.json'

# Read CSV and convert to JSON
data = []
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data.append(row)

# Write to JSON file
with open(json_file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)
