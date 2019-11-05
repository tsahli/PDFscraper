import tika
from tika import parser

raw = parser.from_file('UU Housing Power Drawings.pdf')
content = raw['content']
split = content.split('\n')
circuits = []
panelNames = []

with open('Electrical Equipment Schedule.txt') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        line = line.strip('"')
        if line is not '':
            panelNames.append(line)


for item in split:
    if any(item in split for item in panelNames):
        if '-' in item: # Maybe need to check if item startswith str from panelNames list? Adding too many strings that are not needed
            circuits.append(item)

circuits.sort()

for circuit in circuits:
    print(circuit)