import csv

filename = open('Periodic Table of Elements.csv', 'r')
file = csv.DictReader(filename)

atomic_num = []
element = []
symbol = []
atomic_mass = []

for column in file:
    atomic_num.append(column['AtomicNumber'])
    element.append(column['Element'])
    symbol.append(column['Symbol'])
    atomic_mass.append(column['AtomicMass'])