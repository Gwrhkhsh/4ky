import csv
import re

# Read the txt file
txt_filename = "Data/Toponyms.txt"
with open(txt_filename, "r") as txt_file:
    toponyms = txt_file.read().splitlines()

# Read the csv file
csv_filename = "Data/Uruk_adm_clean.csv"

for toponym in toponyms:
    matching_cases = []
    matching_sources = []

    with open(csv_filename, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)

        for row in csv_reader:
            case = row[0]           # It's "case, source, line, cdli_link, origin, period"
            source = row[1]
            origin = row[4].strip()
            period = row[5].strip()

            # Split the toponym into words
            toponym_words = re.findall(r'\b\w+\b', toponym)

            # Check if all words from the toponym are present in the case
            if all(word in case for word in toponym_words):
                matching_cases.append(case)
                matching_sources.append(source)

    unique_matching_sources = set(matching_sources)

    print(f"{toponym} : {len(matching_cases)} ({len(unique_matching_sources)})")
