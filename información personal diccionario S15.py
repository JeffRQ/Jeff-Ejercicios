# crear un diccionario
informacion_personal = set()

informacion_personal = {"nombre": "Jeff","edad": 34,"ciudad": "Guayaquil", "profesion": "bartender" }

# acceder y modificar valores
informacion_personal["ciudad"] = "Quito"
informacion_personal["profesion"] = "comerciante"

# verificar existencia de clave
informacion_personal["telefono"] = "0994438439"

# eliminar una clave: edad
del(informacion_personal["edad"])


# imprimir diccionario final
print(informacion_personal)

