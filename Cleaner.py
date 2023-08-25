import re

input_file = "inscriptions_2351305.txt"
output_file = "inscriptions_2351305_clean.txt"

# Read lines from the input file
with open(input_file, "r") as file:
    lines = file.readlines()

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

        filtered_lines.append(', '.join([line,
                                         title.strip().replace(',', ''), 
                                         str(index)]))

# Write filtered lines to an output file
with open(output_file, "w") as output_file:
    output_file.write('\n'.join(filtered_lines))

