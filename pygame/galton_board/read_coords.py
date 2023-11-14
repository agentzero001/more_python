import csv

#tuple_pairs = []


with open('coords.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        tuple_pair = row

print([tuple_pair[1]])