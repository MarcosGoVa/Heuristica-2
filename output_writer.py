import csv


def guardar_soluciones_en_csv(solutions, ruta_salida, ambulance_list, tamaño_mapa):
    filas = tamaño_mapa[-1][0]
    columnas = tamaño_mapa[-1][1]
    print(filas)
    print(columnas)


    with open(ruta_salida, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # Escribir el número de soluciones encontradas
        csvwriter.writerow(['N. Sol:', len(solutions)])

        # Escribir las soluciones
        for solution in solutions:
            # Convertir la solución a una lista para escribir en CSV
            mapa = crear_mapa_solucion(filas, columnas, solution, ambulance_list)
            # Escribir cada fila del mapa en el archivo CSV
            for fila in mapa:
                csvwriter.writerow(fila)
            csvwriter.writerow(['*' * 90])


def crear_mapa_solucion(filas, columnas, solucion, ambulance_list):
    mapa=[]
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append("-")
        mapa.append(fila)

    for ambulancia in ambulance_list:
        posicion = solucion.get(ambulancia, '-')
        posicionX = posicion[0]
        posicionY = posicion[1]
        mapa[posicionX-1][posicionY-1] = ambulancia

    
    return mapa