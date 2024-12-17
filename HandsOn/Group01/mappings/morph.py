import os

mapping_path = "HandsOn/Group01/mappings/accidentalidad_mapping-with-links.rml.ttl"

if os.path.exists(mapping_path):
    print(f"El archivo {mapping_path} fue encontrado.")
else:
    print(f"El archivo {mapping_path} no existe.")

import morph_kgc

# Configuración para morph-kgc
config = """
[CONFIGURATION]
output_format = N-TRIPLES

[DataSource1]
mappings = HandsOn/Group01/mappings/radares_mapping.rml.ttl
"""

# Materializar el grafo RDF usando la configuración
rdf_graph = morph_kgc.materialize(config)
rdf_graph.serialize(destination="radares.nt", format="nt")