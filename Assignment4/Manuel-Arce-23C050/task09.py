from rdflib import Graph, Namespace, URIRef

# Crear el grafo y cargar la ontolojia completada
g = Graph()
g.parse('task08_completed.rdf', format="xml")

# Definir namespaces
EX = Namespace("http://example.org/")

# Vinculación de datos: Enlazar personas con una relacion "conoce"
person1 = URIRef(EX.JaneDoe)
person2 = URIRef(EX.JohnSmith)

# Agregar una relación "conoce"
g.add((person1, EX.knows, person2))
g.add((person2, EX.knows, person1))

# Guatdar los cambios
output_path = 'task09_linked.rdf'
g.serialize(destination=output_path, format="pretty-xml")
print("Datos vinculados y guardados en:", output_path)
