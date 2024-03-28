temperaturas = [
    [   # Guayaquil
        [   # Semana 1
            {"día": "Lunes", "temp": 25},
            {"día": "Martes", "temp": 28},
            {"día": "Miércoles", "temp": 26},
            {"día": "Jueves", "temp": 31},
            {"día": "Viernes", "temp": 25},
            {"día": "Sábado", "temp": 32},
            {"día": "Domingo", "temp": 24}
        ],
        [   # Semana 2
            {"día": "Lunes", "temp": 28},
            {"día": "Martes", "temp": 29},
            {"día": "Miércoles", "temp": 27},
            {"día": "Jueves", "temp": 31},
            {"día": "Viernes", "temp": 32},
            {"día": "Sábado", "temp": 27},
            {"día": "Domingo", "temp": 29}
        ],
        [   # Semana 3
            {"día": "Lunes", "temp": 27},
            {"día": "Martes", "temp": 29},
            {"día": "Miércoles", "temp": 28},
            {"día": "Jueves", "temp": 26},
            {"día": "Viernes", "temp": 29},
            {"día": "Sábado", "temp": 31},
            {"día": "Domingo", "temp": 32}
        ],
        [   # Semana 4
            {"día": "Lunes", "temp": 29},
            {"día": "Martes", "temp": 27},
            {"día": "Miércoles", "temp": 26},
            {"día": "Jueves", "temp": 27},
            {"día": "Viernes", "temp": 30},
            {"día": "Sábado", "temp": 28},
            {"día": "Domingo", "temp": 31}
        ]
    ],
    [   # Quitó
        [   # Semana 1
            {"día": "Lunes", "temp": 26},
            {"día": "Martes", "temp": 27},
            {"día": "Miércoles", "temp": 24},
            {"día": "Jueves", "temp": 25},
            {"día": "Viernes", "temp": 27},
            {"día": "Sábado", "temp": 28},
            {"día": "Domingo", "temp": 25}
        ],
        [   # Semana 2
            {"día": "Lunes", "temp": 26},
            {"día": "Martes", "temp": 27},
            {"día": "Miércoles", "temp": 25},
            {"día": "Jueves", "temp": 28},
            {"día": "Viernes", "temp": 24},
            {"día": "Sábado", "temp": 26},
            {"día": "Domingo", "temp": 27}
        ],
        [   # Semana 3
            {"día": "Lunes", "temp": 25},
            {"día": "Martes", "temp": 26},
            {"día": "Miércoles", "temp": 24},
            {"día": "Jueves", "temp": 23},
            {"día": "Viernes", "temp": 25},
            {"día": "Sábado", "temp": 24},
            {"día": "Domingo", "temp": 26}
        ],
        [   # Semana 4
            {"día": "Lunes", "temp": 27},
            {"día": "Martes", "temp": 26},
            {"día": "Miércoles", "temp": 29},
            {"día": "Jueves", "temp": 27},
            {"día": "Viernes", "temp": 28},
            {"día": "Sábado", "temp": 26},
            {"día": "Domingo", "temp": 27}
        ]
    ],
    [   # Machala
        [   # Semana 1
            {"día": "Lunes", "temp": 31},
            {"día": "Martes", "temp": 29},
            {"día": "Miércoles", "temp": 27},
            {"día": "Jueves", "temp": 28},
            {"día": "Viernes", "temp": 30},
            {"día": "Sábado", "temp": 29},
            {"día": "Domingo", "temp": 27}
        ],
        [   # Semana 2
            {"día": "Lunes", "temp": 29},
            {"día": "Martes", "temp": 31},
            {"día": "Miércoles", "temp": 28},
            {"día": "Jueves", "temp": 27},
            {"día": "Viernes", "temp": 29},
            {"día": "Sábado", "temp": 30},
            {"día": "Domingo", "temp": 31}
        ],
        [   # Semana 3
            {"día": "Lunes", "temp": 27},
            {"día": "Martes", "temp": 30},
            {"día": "Miércoles", "temp": 29},
            {"día": "Jueves", "temp": 27},
            {"día": "Viernes", "temp": 28},
            {"día": "Sábado", "temp": 27},
            {"día": "Domingo", "temp": 29}
        ],
        [   # Semana 4
            {"día": "Lunes", "temp": 29},
            {"día": "Martes", "temp": 31},
            {"día": "Miércoles", "temp": 31},
            {"día": "Jueves", "temp": 28},
            {"día": "Viernes", "temp": 27},
            {"día": "Sábado", "temp": 26},
            {"día": "Domingo", "temp": 28}
        ]
    ]
]


#r = temperaturas[0][0][0]["temp"]

# print(r)
# Calcular el promedio de temperaturas para cada ciudad y semana
#for ciudad in temperaturas:
 #   for semana in ciudad:
  #      suma = 0
   #     for dia in semana:
    #        suma += dia['temp']




#for Guayaquil in temperaturas:
 #   for semana in Guayaquil:
  #      suma = 0
   #     for dia in semana:
    #        suma += dia["temp"]

    # promedio = suma / len(semana)
   # print(f"Guayaquil promedio temp: {promedio}")

# Calcular el promedio de temperaturas para cada ciudad y semana
ciudades = ["Guayaquil", "Quitó", "Machala"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f} grados")

ciudades = ["Guayaquil", "Quitó", "Machala"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    suma_temperaturas_ciudad = 0
    cantidad_meses = 0
    for meses_idx, meses in enumerate(ciudad):
        suma_mes = sum(dia["temp"] for dia in meses)
        suma_temperaturas_ciudad += suma_mes
        cantidad_meses += len(meses)

    promedio_ciudad = suma_temperaturas_ciudad / cantidad_meses
    print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}: {promedio_ciudad:.2f} grados")

