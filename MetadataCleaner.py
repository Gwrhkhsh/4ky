import pandas as pd
import re

# Load the CSV file into a DataFrame
input_file = 'Uruk_adm_metadata.csv'
output_file = 'Uruk_adm_metadata_clean.csv'

# Read the CSV file
data = pd.read_csv(input_file)

# Transformations
data['cdli_link'] = 'https://cdli.mpiwg-berlin.mpg.de/artifacts/' + data['artifact_id'].astype(str)
data['period'] = data['period'].apply(lambda x: re.sub(r'\s*\([^)]*\)', '', x) if isinstance(x, str) else x)

# Select the desired columns
output_data = data[['cdli_link', 'designation', 'provenience', 'period']]

# Save the transformed data to a new CSV file
output_data.to_csv(output_file, index=False)

print("Transformation complete. Output saved to", output_file)
