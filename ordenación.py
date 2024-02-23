# Matriz bidimensional 1x15
matriz1_pares = [
    [4],
    [10],
    [2],
    [12],
    [6],
    [14],
    [8],
    [18],
    [16],
    [22],
    [30],
    [28],
    [26],
    [20],
    [24]
]
# imprimir la matriz no ordenada
print("Matriz no ordenada:", matriz1_pares)

# ordenar las filas de la matriz
matriz1_pares.sort(key=lambda filas: min(filas))

# resultado ordenado
print("Matriz ordenada por Valor Minimo en la fila:")
for fila in matriz1_pares:
    print(fila)

print("fin")

