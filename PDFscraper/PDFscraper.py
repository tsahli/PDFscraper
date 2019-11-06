import tika
import PyPDF2
import os
from tika import parser

plans = "UU Housing Power Drawings.pdf"
raw = parser.from_file(plans)
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

#for item in split:
#    if any(item in split for item in panelNames):
#        if '-' in item:
#            circuits.append(item)

for item in split:
    if item.startswith(tuple(panelNames)) and '-' in item:
        itemSplit = item.split()
        for i in itemSplit:
            if i.startswith(tuple(panelNames)) and '-' in i:
                circuits.append(i)

file = open(plans, 'rb')
pdfRotator = PyPDF2.PdfFileReader(file)
pdfWriter = PyPDF2.PdfFileWriter()
for pageNumber in range(pdfRotator.numPages):
    page = pdfRotator.getPage(pageNumber)
    page.rotateClockwise(90)
    pdfWriter.addPage(page)

rotatedPdf = open('rotated.pdf', 'wb')
pdfWriter.write(rotatedPdf)
rotatedPdf.close()

raw = parser.from_file('rotated.pdf')
content = raw['content']
split = content.split('\n')

for item in split:
    if item.startswith(tuple(panelNames)) and '-' in item:
        itemSplit = item.split()
        for i in itemSplit:
            if i.startswith(tuple(panelNames)) and '-' in i and i not in circuits:
                circuits.append(i)

circuits.sort()
os.remove('rotated.pdf')
for circuit in circuits:
    print(circuit)