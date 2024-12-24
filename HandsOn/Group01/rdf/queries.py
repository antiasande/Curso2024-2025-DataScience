from rdflib import Graph
from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd
import matplotlib.pyplot as plt
import time
import folium
import pyproj

# Cargar el archivo RDF proporcionado por el usuario
rdf_file_path_acc = 'with-links/accidentalidad-with-links.nt'
graph_acc = Graph()
graph_acc.parse(rdf_file_path_acc, format='nt')

# Cargar el archivo RDF proporcionado por el usuario
rdf_file_path_rad = 'with-links/radares-with-links.nt'
graph_rad = Graph()
graph_rad.parse(rdf_file_path_rad, format='nt')

# Configuración del endpoint de Wikidata
endpoint_url = "https://query.wikidata.org/sparql"
sparql = SPARQLWrapper(endpoint_url)
sparql.setReturnFormat(JSON)

# Consulta SPARQL para obtener los distritos de Madrid y sus poblaciones a través de Wikidata
query = """
SELECT ?district ?districtLabel ?population WHERE {
  ?district wdt:P31 wd:Q3032114 .  # P31 indica 'instancia de', Q3032114 es 'Distrito de Madrid'
  OPTIONAL { ?district wdt:P1082 ?population . }  # P1082 indica 'población'
  SERVICE wikibase:label { bd:serviceParam wikibase:language "es,en". }
}
"""

# Ejecutar la consulta de distritos y procesar los resultados
sparql.setQuery(query)
time.sleep(1)  # Espera entre consultas
try:
    results = sparql.query().convert()
except Exception as e:
    print(f"Error: {e}")

distritos_madrid = [
    (result["districtLabel"]["value"], result["district"]["value"].split("/")[-1], result.get("population", {}).get("value", "Desconocida"))
    for result in results["results"]["bindings"]
]



# Número de accidentes en cada mes de 2024
meses = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
accidentes_por_mes = []

print("Número de accidentes en cada mes de 2024:")
for mes in meses:
    sparql_query_count_by_month = f"""
    SELECT (COUNT(?accidente) AS ?conteo)
    WHERE {{
        ?accidente <http://dominiowebsemantica.com/ontology/ont#fechaHora> ?fecha .
        FILTER (SUBSTR(STR(?fecha), 6, 2) = "{mes}")
    }}
    """
    results_sameAs = graph_acc.query(sparql_query_count_by_month)
    conteo = sum(int(row[0]) for row in results_sameAs)  # Sumar accidentes
    accidentes_por_mes.append((mes, conteo))
    print(f"Mes: {mes}, Número de accidentes: {conteo}")

# Crear un DataFrame para los accidentes por mes
df_mes = pd.DataFrame(accidentes_por_mes, columns=["Mes", "Accidentes"])

# Accidentalidad por distrito
print("\nAccidentes por cada 1000 personas por distrito: ")
accidentes_distritos = []

for nombreDistrito, codigo, poblacion in distritos_madrid:
    sparql_query_count_by_district = f"""
    SELECT (COUNT(?infoDistrito) AS ?conteo)
    WHERE {{
        ?infoDistrito <http://www.w3.org/2002/07/owl#sameAs> <https://wikidata.org/entity/{codigo}> .
    }}
    """
    results_sameAs = graph_acc.query(sparql_query_count_by_district)
    conteo = sum(int(row[0]) for row in results_sameAs) 
    if poblacion != "Desconocida" and conteo > 0:
        accidentes_por_1000 = float(conteo) * 1000 / int(poblacion)
        accidentes_distritos.append((nombreDistrito, conteo, int(poblacion), accidentes_por_1000, codigo))
        print(f"Distrito: {nombreDistrito}, Número de accidentes: {conteo}, Población: {poblacion}, Accidentes por cada 1000 personas: {accidentes_por_1000:.2f}, Codigo Wikidata: {codigo}")

# Crear un DataFrame para los accidentes por distrito
df_distritos = pd.DataFrame(
    accidentes_distritos,
    columns=["Distrito", "Accidentes", "Población", "Accidentes por 1000", "Código"]
)

# --- Representación gráfica ---
# Gráfico 1: Accidentes por mes
plt.figure(figsize=(10, 6))
plt.plot(df_mes["Mes"], df_mes["Accidentes"], marker="o", linestyle="-", color="orange", label="Accidentes por mes")
plt.title("Número de accidentes por mes en 2024")
plt.xlabel("Mes")
plt.ylabel("Número de accidentes")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.xticks(df_mes["Mes"])  
plt.tight_layout()
plt.show()

# Gráfico 2: Accidentes por cada 1000 habitantes por distrito
plt.figure(figsize=(14, 8))
df_distritos_sorted = df_distritos.sort_values(by="Accidentes por 1000", ascending=False)
plt.bar(df_distritos_sorted["Distrito"], df_distritos_sorted["Accidentes por 1000"], color="orange")
plt.title("Accidentes por cada 1000 personas por distrito")
plt.ylabel("Accidentes por cada 1000 habitantes")
plt.xlabel("Distrito")
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()


# Número de accidentes por sexo
sexos = ["male", "female"]
conteos = []

for sexo in sexos:
    sparql_query_count_by_month = """
    SELECT (COUNT(?accidente) AS ?conteo)
    WHERE {{
      ?accidente <http://dominiowebsemantica.com/ontology/ont#sexo> ?sexo .
      
      FILTER (?sexo = "{sexo}")
    }}
    """.format(sexo=sexo)
    results_sameAs = graph_acc.query(sparql_query_count_by_month)

    sameAs_results = [int(row["conteo"]) for row in results_sameAs]
    conteos.append(sameAs_results[0]) if sameAs_results else conteos.append(0)

plt.figure(figsize=(6, 6))
plt.pie(conteos, labels=sexos, autopct='%1.1f%%', startangle=90, colors=['#ffcc66', '#ff9966'])
plt.title("Distribución de Accidentes por Sexo")
plt.show()



# Consulta SPARQL para obtener los tipos de radares y su cantidad
sparql_query_radar_types = """
SELECT ?tipo (COUNT(?radar) AS ?cantidad)
WHERE {
  ?radar <http://dominiowebsemantica.com/ontology/ont#tipo> ?tipo .
}
GROUP BY ?tipo
"""

# Ejecutar la consulta
print("Tipos de radares y su cantidad:")
tipos = []
cantidades = []
results_radar_types = graph_rad.query(sparql_query_radar_types)
for row in results_radar_types:
    print(f"Tipo: {row.tipo}, Cantidad: {row.cantidad}")
    tipos.append(str(row.tipo))  # Agregar tipo de radar a la lista
    cantidades.append(int(row.cantidad))  # Agregar cantidad de radares a la lista

plt.figure(figsize=(7, 7))
plt.pie(cantidades, labels=tipos, autopct='%1.1f%%', startangle=90, colors=['#ffcc66', '#ff9966'])
plt.title('Distribución de tipos de radares')
plt.axis('equal')  # Para que el gráfico sea un círculo perfecto
plt.show()



# Consulta SPARQL para obtener las carreteras y sus enlaces a Wikidata
sparql_query_carreteras = """
SELECT DISTINCT ?nombre ?wikidataLink
WHERE {
  ?carretera <http://dominiowebsemantica.com/ontology/ont#carretera> ?nombre .
  ?carretera <http://www.w3.org/2002/07/owl#sameAs> ?wikidataLink .
  ?carretera <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dominiowebsemantica.com/ontology/ont#InfoCarretera> .
}
"""

# Ejecutar la consulta
print("Carreteras y sus enlaces a Wikidata:")
results_carreteras = graph_rad.query(sparql_query_carreteras)

# Mostrar resultados
for row in results_carreteras:
    print(f"Carretera: {row.nombre}, Wikidata Link: {row.wikidataLink}")   
    

# Consulta SPARQL para obtener las coordenadas de los radares (coordenadaX y coordenadaY)
sparql_query_coordenadas_radar = """
SELECT ?radar ?coordenadaX ?coordenadaY
WHERE {
  ?radar <http://dominiowebsemantica.com/ontology/ont#coordenadaX> ?coordenadaX .
  ?radar <http://dominiowebsemantica.com/ontology/ont#coordenadaY> ?coordenadaY .
  FILTER (datatype(?coordenadaX) = <http://www.w3.org/2001/XMLSchema#decimal>) .
  FILTER (datatype(?coordenadaY) = <http://www.w3.org/2001/XMLSchema#decimal>) .
}
"""

# Ejecutar la consulta
print("\nCoordenada X (longitud) y coordenada Y (latitud):")
results_coordenadas_radar = graph_rad.query(sparql_query_coordenadas_radar)

# Mostrar resultados
for row in results_coordenadas_radar:
    print(f"Coordenada X (longitud): {row.coordenadaX}, Coordenada Y (latitud): {row.coordenadaY}")


### Creación mapa de Accidentes y Radares

## CONSULTA ACCIDENTES
sparql_long_lat = """
SELECT ?accidente ?long ?lat
WHERE {{
  ?accidente <http://www.w3.org/2003/01/geo/wgs84_pos#long> ?long .
  ?accidente <http://www.w3.org/2003/01/geo/wgs84_pos#lat> ?lat .
}}
LIMIT 800
"""

# Ejecutar la consulta
results = graph_acc.query(sparql_long_lat)


lista_coordenadas_acc = []
# Procesar y mostrar los resultados
for row in results:
  longitud = float(row.long)
  latitud = float(row.lat)
  lista_coordenadas_acc += [(longitud, latitud)]


## CONSULTA RADARES
sparql_longitudes_radares= """
SELECT ?radar ?X ?Y
WHERE {{
  ?radar <http://dominiowebsemantica.com/ontology/ont#coordenadaX> ?X .
  ?radar <http://dominiowebsemantica.com/ontology/ont#coordenadaY> ?Y .
}}
"""


# Ejecutar la consulta
results = graph_rad.query(sparql_longitudes_radares)


lista_coordenadas_rad = []
# Procesar y mostrar los resultados
for row in results:
  longitud = float(row.X)
  latitud = float(row.Y)
  lista_coordenadas_rad += [(latitud, longitud)]



def utm_to_folium_format(utm_easting, utm_northing, utm_zone):
    """
    Convierte coordenadas UTM (Este y Norte) a coordenadas geográficas (Latitud, Longitud) para usar en Folium.

    Args:
    utm_easting (float): Coordenada Este (X) en UTM.
    utm_northing (float): Coordenada Norte (Y) en UTM.
    utm_zone (int): Zona UTM.

    Returns:
    tuple: (latitud, longitud) en formato decimal (WGS84), listo para usar en Folium.
    """

    # Definir el proyector UTM y WGS84
    utm_proj = pyproj.Proj(proj="utm", zone=utm_zone, datum="WGS84")
    wgs84_proj = pyproj.Proj(proj="latlong", datum="WGS84")

    # Convertir las coordenadas UTM a coordenadas geográficas (latitud, longitud)
    longitud, latitud = pyproj.transform(utm_proj, wgs84_proj, utm_easting, utm_northing)

    return latitud, longitud


coordenadas_folium_acc = []

for tupla in lista_coordenadas_acc:
    coordenadas_folium_acc.append(utm_to_folium_format(tupla[0], tupla[1], 30))


def generar_mapa(coordenadas_accidentes, coordenadas_radares, nombre_mapa="mapa.html"):
    if not coordenadas_accidentes and not coordenadas_radares:
        print("Las listas de coordenadas están vacías.")
        return

    # Usar la primera coordenada de accidentes o radares como centro del mapa
    centro = coordenadas_accidentes[0] if coordenadas_accidentes else coordenadas_radares[0]

    # Crear el mapa centrado en la primera coordenada
    mapa = folium.Map(location=centro, zoom_start=13)

    # Añadir marcadores de accidentes al mapa
    for i, (lat, lon) in enumerate(coordenadas_accidentes):
        folium.Marker(
            location=[lat, lon],
            popup=f"Accidente {i+1}: ({lat}, {lon})",
            icon=folium.Icon(icon="exclamation-sign", color="red")
        ).add_to(mapa)

    # Añadir marcadores de radares al mapa
    for i, (lat, lon) in enumerate(coordenadas_radares):
        folium.Marker(
            location=[lat, lon],
            popup=f"Radar {i+1}: ({lat}, {lon})",
            icon=folium.Icon(icon="camera", color="blue")
        ).add_to(mapa)

    # Guardar el mapa como un archivo HTML
    mapa.save(nombre_mapa)
    print(f"Mapa guardado como {nombre_mapa}")

# Generar el mapa
generar_mapa(coordenadas_folium_acc, lista_coordenadas_rad)

