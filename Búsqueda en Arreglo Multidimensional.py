# Definir la matriz bidimensional 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Función para buscar un valor específico en la matriz
def buscar_valor(matriz, valor_buscado):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_buscado:
                return i, j  # Retorna la posición (fila, columna) del valor encontrado
    return None  # Si el valor no se encuentra, retorna None

# Valor a buscar en la matriz
valor_buscado = 5

# Llamada a la función de búsqueda
posicion = buscar_valor(matriz, valor_buscado)

# Verificación y mensaje de resultado
if posicion:
    print(f"El valor {valor_buscado} se encontró en la posición {posicion} (fila {posicion[0]}, columna {posicion[1]}).")
else:
    print(f"El valor {valor_buscado} no se encontró en la matriz.")
