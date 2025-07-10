import pyodbc  # (1) Importa la librería para conectar con SQL Server
import csv
def obtener_tabla():
    # (2) Define el string de conexión a la base de datos
    conexion = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=constec.ar;'
        'DATABASE=constecw_db;'
        'UID=constecw_us;'
        'PWD=08x19^gQv'
    )

    # (3) Crea un cursor para ejecutar consultas
    cursor = conexion.cursor()

    # (4) Ejecuta la consulta SQL para obtener todos los datos de la tabla Conocimiento
    cursor.execute("SELECT * FROM Conocimiento")

    # (5) Obtiene los nombres de las columnas de la tabla
    columnas = [desc[0] for desc in cursor.description]

    # (6) Guarda todos los registros como lista de diccionarios
    datos = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]

    # (7) Cierra la conexión
    cursor.close()
    conexion.close()

    # (8) Muestra los datos por pantalla 
    print(datos)

    return datos

def guardar_csv(datos, nombre_archivo="conocimiento.csv"): #AGREGADO
    if not datos:
        return
    columnas = list(datos[0].keys())
    with open(nombre_archivo, mode="w", newline='', encoding='utf-8') as archivo:
        writer = csv.DictWriter(archivo, fieldnames=columnas)
        writer.writeheader()
        writer.writerows(datos)

def obtener_contexto():
    datos = obtener_tabla()

    if not datos:
        return "No se pudo obtener información de la base."

    columnas = list(datos[0].keys())
    contexto = "Base de conocimientos:\n"

    for fila in datos:
        fila_texto = " | ".join(f"{col}: {fila[col]}" for col in columnas)
        contexto += "- " + fila_texto + "\n"

    return contexto