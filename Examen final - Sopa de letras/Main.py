import json

def leer_archivo(file_path):
    """
    Lee el archivo .txt y devuelve la sopa de letras y las palabras a buscar.
    """
    with open(file_path, "r") as file:
        lines = file.readlines()
        
    sopa = [line.strip() for line in lines[:5]]  # sopa tiene 5 filas
    palabras = [line.strip() for line in lines[6:]]  # palabras despues de la linea 6
    
    return sopa, palabras

def buscar_palabra(sopa, palabra):
    """
    llama las otra funciones de buscar las palabras en todas las direcciones.
    """
    for i in range(len(sopa)):
        for j in range(len(sopa[i])):
            palabra_mayus= palabra.upper()
            if buscar_horizontales(sopa, palabra_mayus, i, j) or \
               buscar_verticales(sopa, palabra_mayus, i, j) or \
               buscar_diagonales(sopa, palabra_mayus, i, j):
                return True
    return False

def buscar_horizontales(sopa, palabra, fila, columna):
    """
    Verifica si la palabra se encuentra en la fila de izquierda a derecha o de derecha a izquierda.
    """
    # De izquierda a derecha
    if sopa[fila][columna:columna+len(palabra)] == palabra:
        return True
    # De derecha a izquierda
    if sopa[fila][columna:columna-len(palabra):-1] == palabra:
        return True
    return False
#el .join convierte la lista de caracteres en una cadena de texto ej:   lista= ["1", "2"]  Lista.join ="12"
def buscar_verticales(sopa, palabra, fila, columna):
    """
    Verifica si la palabra se encuentra en la columna de arriba hacia abajo o de abajo hacia arriba.
    """
    # De arriba hacia abajo
    if fila + len(palabra) <= len(sopa) and "".join([sopa[fila+k][columna] for k in range(len(palabra))]) == palabra:
        return True
    # De abajo hacia arriba
    if fila - len(palabra) >= -1 and "".join([sopa[fila-k][columna] for k in range(len(palabra))]) == palabra:
        return True
    return False

def buscar_diagonales(sopa, palabra, fila, columna):
    """
    Verifica si la palabra se encuentra en las diagonales.
    """
    # Diagonal de arriba hacia abajo y de izquierda a derecha
    if fila + len(palabra) <= len(sopa) and columna + len(palabra) <= len(sopa[0]):
        if "".join([sopa[fila+k][columna+k] for k in range(len(palabra))]) == palabra:
            return True
    # Diagonal de abajo hacia arriba y de izquierda a derecha
    if fila - len(palabra) >= -1 and columna + len(palabra) <= len(sopa[0]):
        if "".join([sopa[fila-k][columna+k] for k in range(len(palabra))]) == palabra:
            return True
    # Diagonal de abajo hacia arriba y de derecha a izquierda
    if fila - len(palabra) >= -1 and columna - len(palabra) >= -1:
        if "".join([sopa[fila-k][columna-k] for k in range(len(palabra))]) == palabra:
            return True
    # Diagonal de arriba hacia abajo y de derecha a izquierda
    if fila + len(palabra) <= len(sopa) and columna - len(palabra) >= -1:
        if "".join([sopa[fila+k][columna-k] for k in range(len(palabra))]) == palabra:
            return True

    return False
def generar_reporte(sopa, palabras):
    """
    genera un reporte de las palabras encontradas y no encontradas en la sopa.
    """
    resultado = {}
    for palabra in palabras:
        resultado[palabra] = buscar_palabra(sopa, palabra)

    return resultado
def guardar_reporte(reporte, output_file):
    """
    guarda el reporte en formato JSON.
    """
    with open(output_file, "w") as json_file:
        json.dump(reporte, json_file, indent=4)
# aqui se llaman las funciones para la ruta del archivo de entrada , Guardar  y generar el reporte en un archivo JSON y  Leer la sopa de letras y las palabras a buscar
file_path = "sopa_de_letras.txt"
sopa, palabras = leer_archivo(file_path)
reporte = generar_reporte(sopa, palabras)
guardar_reporte(reporte, "reporte_sopa_de_letras.json")
