line_sets = []
full_set = []
import csv
with open('list_to_csv.csv') as inp:
    lines = inp.readlines()

    for i in range(0, len(lines)):
        # strip for precaution
        tokens = [w.strip() for w in lines[i].split(',')[0:2]]
        tmp_set = set(tokens)

        if tmp_set not in line_sets:
            full_set.append(lines[i].split(','))
            line_sets.append(tmp_set)

with open('otsort.csv', 'w') as out:
    for line in full_set:
        out.write(','.join(line))