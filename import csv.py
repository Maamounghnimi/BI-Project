import pandas as pd

# Load the CSV file into a DataFrame
input_file_path = r'C:\Users\ASUS\Desktop\DBMS\transactions_info.csv'
output_file_path = r'C:\Users\ASUS\Desktop\DBMS\transactions_info_clean.csv'

# Specify the column you want to sort by
column_to_sort = 'Transaction ID'  # Replace with the actual column name you want to sort

df = pd.read_csv(input_file_path)

# Sort the DataFrame by the specified column
df_sorted = df.sort_values(by=column_to_sort)

# Save the sorted DataFrame to a new CSV file
df_sorted.to_csv(output_file_path, index=False)

print(f'Column "{column_to_sort}" sorted. Output saved to: {output_file_path}')
