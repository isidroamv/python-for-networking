""" CSV """
import csv

with open('data/text.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
	pass
        #print(row['nombre'], row['edad'])













""" JSON """

import json

with open('data/text.json') as data_json:    
    data = json.load(data_json)
    #print data
    pass
    #print(data['edad'], data['apellidos']['apellido_paterno'])













""" XML """

import xml.etree.ElementTree as ET
tree = ET.parse('data/text.xml')
root = tree.getroot()
for child in root:
    pass
    #print(child.text)
