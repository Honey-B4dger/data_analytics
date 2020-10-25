from matplotlib import pyplot as plt
import csv

with open('assets/titanic3.csv', 'r') as f:
    data = list(csv.reader(f))

print(data)
