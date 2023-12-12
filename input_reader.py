import sys

def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
    
    # Extracción de filas x columnas
    filas, columnas = map(int, lineas[0].strip().split('x'))
    filas_columnas = [(i, j) for i in range(1, filas + 1) for j in range(1, columnas + 1)]

    # Extracción de plazas con conexión eléctrica
    plazas_electricas = lineas[1].strip()[3:]  # Excluir "PE:(" del inicio y ")" del final
    tuplas_str = plazas_electricas[1:-1].split(")(")

    # Convertir las cadenas de tuplas en tuplas reales
    plazas_electricas = [tuple(map(int, tupla.split(','))) for tupla in tuplas_str]

    # Extracción de información de vehículos
    vehiculos = lineas[2:]

    return filas_columnas, plazas_electricas, vehiculos


def procesar_vehiculos(vehiculos) -> list:
    resultado = []
    for vehiculo in vehiculos:
        info = vehiculo.strip().split('-')
        id_vehiculo = info[0]
        tipo = info[1]
        congelador = info[2][0]
        resultado.append(f"{id_vehiculo}-{tipo}-{congelador}")
    
    return resultado


def main():
    if len(sys.argv) != 2:
        print("Uso: python CSPParking.py <ruta_del_archivo>")
        sys.exit(1)

    # Obtener la ruta del archivo desde la línea de comandos
    ruta_archivo = sys.argv[1]

    filas_columnas, plazas_electricas, vehiculos = leer_archivo(ruta_archivo)

    return filas_columnas, plazas_electricas, procesar_vehiculos(vehiculos)






if __name__ == "__main__":
    main()
