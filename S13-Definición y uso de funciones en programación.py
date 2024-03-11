# función de calcular promedio de temperaturas de una ciudad
# en un intervalo de tiempo

def calcular_tempe(datos, ciudad, semana_inicial, semana_final):
    numero_items = 0  # Variable para almacenar el total de items
    suma_tempe = 0  # Variable que acumula la sumatoria de las temperaturas
    for i in range(len(datos[ciudad])):  # se obtiene el número de elementos en la posición
        if i  >= semana_inicial and i<= semana_final:
            for j in range(len(datos[ciudad][i])):
                suma_tempe=suma_tempe+datos[ciudad][i][j]["temp"]
                numero_items=numero_items+1
                print(datos[ciudad][i][j])
    promedio = suma_tempe/numero_items
    return promedio

# datos de temperaturas

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


calculo_prome = calcular_tempe(temperaturas, 1,0,3)
print(f" promedio de ciudad {calculo_prome: .2f}")
