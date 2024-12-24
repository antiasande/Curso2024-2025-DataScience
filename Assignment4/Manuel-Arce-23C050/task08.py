from rdflib import Graph, Namespace, Literal, RDF

# Crear el grafo y cargar la ontologia modificada
g = Graph()
g.parse('task06_modified.rdf', format="xml")

# Definir namespaces
EX = Namespace("http://example.org/")
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")

# Completar datos faltantes
# Añadir apellido si no existe
for s, p, o in g.triples((None, RDF.type, EX.Person)):
    if not (s, VCARD.Family, None) in g:
        g.add((s, VCARD.Family, Literal("ApellidoFaltante")))

# Completar nombre completo si no existe
for s, p, o in g.triples((None, RDF.type, EX.Person)):
    if not (s, VCARD.FN, None) in g:
        given_name = g.value(s, VCARD.Given)
        family_name = g.value(s, VCARD.Family)
        if given_name and family_name:
            g.add((s, VCARD.FN, Literal(f"{given_name} {family_name}")))

# Guardar los cambioa
output_path = 'task08_completed.rdf'
g.serialize(destination = output_path, format = "pretty-xml")
print("Datos completados y guardados en:", output_path)
