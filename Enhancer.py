import re
import csv

input_file = "Uruk_adm.txt"
output_file = "Uruk_adm_clean.txt"
csv_file = "Uruk_adm_metadata_clean.csv"

# Read lines from the input file
with open(input_file, "r") as file:
    lines = file.readlines()

# Read CSV file into a dictionary for easy access
csv_data = {}
with open(csv_file, "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        csv_data[row["designation"]] = {k: v for k, v in row.items() if k != "designation"}

# Process lines and create arrays for non-empty and filtered lines
filtered_lines = []
for line in lines:
    line = line.strip()

    if line and line.startswith('&'):
        if "=" in line:
            title = line.split('=')[1]
        else:
            title = line
        index = 0

    elif line and not line.startswith('@') and not line.startswith('$') and not line.startswith('#') and not line.startswith('>'):
        index += 1

        line = line.replace('#', '').replace('?', '').replace('X', '?').replace('[...]', '...').replace(' ,', '').strip()      # normalization 1
        line = re.sub(r'~[a-f0-9]*', '', line)                                                                                 # normalization 2
        line = re.sub(r'^.*?\s', '', line)

        metadata_entry = csv_data.get(title.strip())
        if metadata_entry:
            metadata_values = ", ".join(metadata_entry.values())
        else:
            # If no metadata entry found, add empty metadata values
            num_metadata_columns = len(next(iter(csv_data.values())))
            metadata_values = ", ".join(["" for _ in range(num_metadata_columns)])

        filtered_lines.append(', '.join([line, title.strip().replace(',', ''), str(index), metadata_values]))

# Write filtered lines to an output file
with open(output_file, "w") as output_file:
    output_file.write('\n'.join(filtered_lines))
