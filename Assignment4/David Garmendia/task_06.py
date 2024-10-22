# UPM - KNOWLEDGE GRAPHS
# DAVID GARMENDIA GARCÍA

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS

g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere/#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)

g.parse(github_storage+"/rdf/example5.rdf", format="xml")

ns = Namespace("http://somewhere/#")

# Ejercicio: 6.1
g.add((ns.University, RDF.type, RDFS.Class))

for s, p, o in g:
    print(s, p, o)

# Ejercicio: 6.2
g.add((ns.Researcher, RDFS.subClassOf, ns.Person))
for s, p, o in g:
  print(s, p, o)

# Ejercicio: 6.3
jane_smithers = ns.JaneSmithers
g.add((jane_smithers, RDF.type, ns.Researcher))
for s, p, o in g:
  print(s, p, o)

# Ejercicio: 6.4
schema = Namespace("https://schema.org/")
g.namespace_manager.bind('schema', schema, override=False)

g.add((jane_smithers, schema.email, Literal("janesmithers@example.com")))
g.add((jane_smithers, schema.name, Literal("Jane Smithers")))
g.add((jane_smithers, schema.givenName, Literal("Jane")))
g.add((jane_smithers, schema.familyName, Literal("Smithers")))

for s, p, o in g:
    print(s, p, o)

# Ejercicio: 6.5
example = Namespace("https://example.org/")
g.namespace_manager.bind('example', example, override=False)

john_smith = ns.JohnSmith

g.add((john_smith, example.worksAt, example.UPM))

for s, p, o in g:
    print(s, p, o)

# Ejercicio: 6.6
foaf = Namespace("http://xmlns.com/foaf/0.1/")
g.namespace_manager.bind('foaf', foaf, override=False)

g.add((john_smith, foaf.knows, jane_smithers))

for s, p, o in g:
    print(s, p, o)
