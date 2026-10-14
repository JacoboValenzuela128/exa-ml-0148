import sys
import os
import pandas as pd
import io

# Permitir importar dicc_0148.py desde la subcarpeta hermana 'datos-de-entrada-ml-0148'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'datos-de-entrada-ml-0148')))
import dicc_0148 # type: ignore

encabezado_pie = "Arath Valenzuela Machine Learning pandas, NC 0148"
print(encabezado_pie)

# Variable para almacenar las salidas y guardarlas en el archivo .md
contenido_md = []
contenido_md.append(f"# Reporte de Análisis de Datos - Pandas\n\n`{encabezado_pie}`\n")

def registrar(titulo, contenido):
    """Muestra el resultado en terminal y lo formatea para el archivo Markdown."""
    print(f"\n--- {titulo} ---")
    print(contenido)
    contenido_md.append(f"## {titulo}\n```text\n{contenido}\n```\n")

# 1. Convertir diccionario a DataFrame
df = pd.DataFrame(dicc_0148.datos_carnicerias)
registrar("1. DataFrame Convertido", df)

# 2. Información Estructural
registrar("2.1 Primeras Filas (head)", df.head(2))
registrar("2.2 Últimas Filas (tail)", df.tail(2))
registrar("2.3 Dimensiones (Filas, Columnas)", df.shape)
registrar("2.4 Tipos de Datos por Columna", df.dtypes)

# Capturar salida de df.info()
buffer = io.StringIO()
df.info(buf=buffer)
registrar("2.5 Información General (info)", buffer.getvalue())

# 3. Estadísticas Generales de una Columna Numérica (Kg_dia)
registrar("3. Estadísticas Generales de la Columna 'Kg_dia'", df['Kg_dia'].describe())

# 4. Ordenar Ascendente por Cortes
df_asc_cortes = df.sort_values(by="Cortes", ascending=True)
registrar("4. Ordenar Ascendente por Cortes", df_asc_cortes)

# 5. Ordenar Descendente por Kg_dia
df_desc_kg = df.sort_values(by="Kg_dia", ascending=False)
registrar("5. Ordenar Descendente por Kg_dia", df_desc_kg)

# 6. Guardar el archivo resultados-ml-0148.md dentro de resultados-0148
carpeta_resultados = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'resultados-0148'))
os.makedirs(carpeta_resultados, exist_ok=True)
ruta_archivo_md = os.path.join(carpeta_resultados, "resultados-ml-0148.md")

contenido_md.append(f"`{encabezado_pie}`")

with open(ruta_archivo_md, "w", encoding="utf-8") as f:
    f.write("\n".join(contenido_md))

print(f"\n[ÉXITO] Archivo generado correctamente en: {ruta_archivo_md}")
print("Arath Valenzuela con Machine Learning y pandas") 
print("NC: 0148")