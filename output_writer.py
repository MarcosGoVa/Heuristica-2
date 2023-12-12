import csv


def guardar_soluciones_en_csv(solutions, ruta_salida, ambulance_list):
    with open(ruta_salida, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # Escribir el número de soluciones encontradas
        csvwriter.writerow(['N. Sol:', len(solutions)])

        # Escribir las soluciones
        for solution in solutions:
            # Convertir la solución a una lista para escribir en CSV
            row = [solution.get(ambulance, '-') for ambulance in ambulance_list]
            csvwriter.writerow(row)