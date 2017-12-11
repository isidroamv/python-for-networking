
nombres = [
    ["Aldo","Vengas",24,"Developer","negro"],
    ["Isidro","Martinez",26,"Developer","blanco"],
    ["Karla","Solis",25,"Developer","rojo"]
]

import csv
with open('data_write/text.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter.writerow(nombres[0])
    spamwriter.writerow(nombres[1])


import json
diccionario = {
    "nombre": "Aldo",
    "edad": 25,
    "colores": ["negro", "blanco"],
    "apellidos": {
        "apellido_paterno": "Venegas",
        "apeliido_materno": "---"
    }
}

import json
with open('data_write/text.json', 'w') as f:
    json.dump(diccionario, f)