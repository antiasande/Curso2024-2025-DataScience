from rdflib import Graph, Namespace, Literal, RDF, RDFS, URIRef

# Crear un grafo RDF
g = Graph()

# Definir namespaces comunes
EX = Namespace("http://example.org/")
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")

# Cargar la ontología existente desde el archivo RDF
ontology_path = '../course_materials/rdf/example1.rdf'  # Ruta relativa
g.parse(ontology_path, format="xml")

# Modificación de una ontología existente
# 1. Añadir una nueva clase en la ontología
new_class = URIRef(EX.Person)
g.add((new_class, RDF.type, RDFS.Class))

# 2. Crear un nuevo recurso (una persona) y agregar propiedades
person = URIRef(EX.JaneDoe)
g.add((person, RDF.type, EX.Person))
g.add((person, VCARD.FN, Literal("Jane Doe")))
g.add((person, VCARD.Given, Literal("Jane")))
g.add((person, VCARD.Family, Literal("Doe")))

# 3. Actualizar una propiedad existente
for s, p, o in g.triples((None, VCARD.FN, Literal("John Smith"))):
    g.set((s, VCARD.FN, Literal("Johnathan Smith")))

# Guardar la ontología modificada en un archivo
output_path = 'task06_modified.rdf'
g.serialize(destination=output_path, format="pretty-xml")
print("Archivo modificado guardado como:", output_path)
