from rdflib import Graph, Namespace, RDF

# Crear el grafo y cargar la ontología modificada
g = Graph()
g.parse('task06_modified.rdf', format="xml")

# Definir los namespaces
EX = Namespace("http://example.org/")
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")

# Consulta 1: Obtener todas las personas y sus nombres completos
print("Consulta 1: Personas y sus nombres completos")
for s, p, o in g.triples((None, RDF.type, EX.Person)):
    for _, _, name in g.triples((s, VCARD.FN, None)):
        print(f"Persona: {s}, Nombre Completo: {name}")

# Consulta 2: Obtener todas las personas y sus apellidos
print("\nConsulta 2: Personas y sus apellidos")
for s, p, o in g.triples((None, VCARD.Family, None)):
    print(f"Persona: {s}, Apellido: {o}")
