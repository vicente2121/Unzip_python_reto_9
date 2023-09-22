import psycopg2
import openpyxl


connection = psycopg2.connect(
    database="Reto9DB",
    user="postgres",
    password="Contraseña",
    host="localhost",
    port="5432"
)


archivo_excel = "direccion del fichero .xlsx"

nombre_esquema = "Reto_9"

nombre_tabla = "stage"


libro_de_trabajo = openpyxl.load_workbook(archivo_excel)
hoja_de_trabajo = libro_de_trabajo.active


nombres_columnas = [columna.value for columna in hoja_de_trabajo[1]]


consulta_creacion_tabla = f"""
    CREATE TABLE IF NOT EXISTS {nombre_esquema}.{nombre_tabla} (
        {", ".join([f'"{nombre}" TEXT' for nombre in nombres_columnas])}
    )
"""


cursor = connection.cursor()
consulta_creacion_esquema = f"CREATE SCHEMA IF NOT EXISTS {nombre_esquema}"
cursor.execute(consulta_creacion_esquema)


cursor.execute(consulta_creacion_tabla)


datos_a_insertar = []
for fila in hoja_de_trabajo.iter_rows(min_row=2, values_only=True):
    datos_a_insertar.append(fila)


consulta_insercion = f"""
    INSERT INTO {nombre_esquema}.{nombre_tabla} ({", ".join([f'"{nombre}"' for nombre in nombres_columnas])})
    VALUES ({", ".join(["%s" for _ in nombres_columnas])})
"""

cursor.executemany(consulta_insercion, datos_a_insertar)

connection.commit()


cursor.close()
connection.close()

print("Importación completada con éxito.")
