# Abrir el archivo en modo lectura
archivo = open("My_notes.txt", "r")

# Leer los datos del archivo y almacenarlos en una variable
datos_my_notes = archivo.read()

archivo.close()

# Abrir el archivo en modo escritura
archivo = open("My_notes.txt", "w")

# Escribir el nuevo contenido en el archivo, junto con el contenido anterior
archivo.write(datos_my_notes + "\n")
archivo.write("Celular: 0994438439")

# Cerrar el archivo después de la escritura
archivo.close()

# Abrir el archivo nuevamente en modo lectura
archivo = open("My_notes.txt", "r")

# Leer los datos del archivo actualizado y almacenarlos en una variable
contenido_actualizado = archivo.read()

# Imprimir actializacion
print(contenido_actualizado)

# Cerrar el archivo después de la última lectura
archivo.close()