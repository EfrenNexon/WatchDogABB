# Importamos modulo para trabajar con funciones del sistema
import os
# Importamos modulo para trabajar con los PDFs
import fitz
# Importamos modulo para trabajar con tiempos
import time
# Creamos la funcion para crear imagenes
def make_pictures(list_files, path_pdf, path_db, kind):
    # Pausamos la ejecucion
    time.sleep(1)
    # Si hay un archivo nuevo...
    if (list_files != os.listdir(path_pdf)):
        # Recorremos los archivos actuales
        for file in os.listdir(path_pdf):
            # Si el archivo no esta registrado lo mostramos
            if (file not in list_files):
                # Verificamos que el archivo sea un PDF
                if (".pdf" in file):
                    # Abrimos el archivo pdf
                    doc = fitz.open(path_pdf + '\\' + file)
                    # Recorremos cada pagina
                    for pg in range(doc.pageCount):
                        # Declaramos la pagina
                        page = doc[pg]
                        # Rotamos la pagina
                        rotate = int(0)
                        # Ajustamos el factor de escala para la dimension de la imagen en x
                        zoom_x = 10.0
                        # Ajustamos el factor de escala para la dimension de la imagen en y
                        zoom_y = 10.0
                        # Definimos los valores de ajuste de la imagen
                        trans = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate)
                        # Definimos la pagina con sus valores
                        pm = page.get_pixmap(matrix=trans, alpha=False)
                        # Creamos la imagen
                        pm.save(path_db + "\\DB\\" + kind + "\\" + file.replace('.pdf', '.png'))
                    # Mostramos un mensaje de archivo creado
                    print("Archivo registrado: " + file)    
    # Actualizamos la lista
    return os.listdir(path_pdf)
# Creamos la funcion principal
def main():
    # Abrimos el archivo de ajustes
    with open("settings.txt", "r") as file:
        # Recorremos cada una de las lineas del archivo
        for line in file.readlines():
            # Si la linea es de la ruta de los shipshorts...
            if (line.find("PATH SHIPSHORTS = ") != -1):
                # Almacenamos la ruta de los shipshorts
                SOURCE_PATH_SHIPSHORTS = line.strip("PATH SHIPSHORTS = ").replace('\n', '')
            # Si la linea es de la ruta de los empowers...
            if (line.find("PATH EMPOWERS = ") != -1):
                # Almacenamos la ruta de los empowers
                SOURCE_PATH_EMPOWERS = line.strip("PATH EMPOWERS = ").replace('\n', '')
            # Si la linea es de la ruta la base de datos...
            if (line.find("PATH DATA BASE = ") != -1):
                # Almacenamos la ruta de los empowers
                DB_PATH = line.strip("PATH DATA BASE = ").replace('\n', '')
    # Almacenamos el nombre de los archivos shipshorts existentes
    files_shipshorts = os.listdir(SOURCE_PATH_SHIPSHORTS)
    # Almacenamos el nombre de los archivos empowers existentes
    files_empowers = os.listdir(SOURCE_PATH_EMPOWERS)
    # Creamos un bucle infinito
    while True:
        # Llamamos la funcion para crear imagenes de los shipshorts
        files_shipshorts = make_pictures(files_shipshorts, SOURCE_PATH_SHIPSHORTS, DB_PATH, "shipshorts")
        # Llamamos la funcion para crear imagenes de los empowers
        files_empowers = make_pictures(files_empowers, SOURCE_PATH_EMPOWERS, DB_PATH, "empowers")
# Creamos un punto de acceso
if __name__ == "__main__":
    # Llamamos a la funcion principal
    main()