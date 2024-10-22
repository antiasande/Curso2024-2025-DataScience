# UPM - KNOWLEDGE GRAPHS
# DAVID GARMENDIA GARCÍA

github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2024-2025/master/Assignment4/course_materials"

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere/#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

# Ejercicio: 7.1
from rdflib.plugins.sparql import prepareQuery
ns = Namespace("http://somewhere/#")
rdfs = Namespace("http://www.w3.org/200/01/rdf-schema#")
q1 = prepareQuery("""
    SELECT ?subclass WHERE {
        ?subclass rdfs:subClassOf* ns:Livingthing .
    }""",
    initNs = {"ns": ns, "rdfs": rdfs})

for subclass in g.subjects(RDFS.subClassOf, ns.LivingThing):
    print(subclass)
for r in g.query(q1):
    print(r.subclass)

# Ejercicio: 7.2
from rdflib.namespace import RDF as rdf
q2 = prepareQuery("""
    SELECT ?individual WHERE {
        ?class rdfs:subClassOf* ns:Person .
        ?individual rdf:type ?class .
    }""",
    initNs = {"ns": ns, "rdf": rdf, "rdfs": rdfs})

for r in g.query(q2):
    print(r.individual)

# Ejercicio: 7.3
q3 = prepareQuery("""
    SELECT ?individual WHERE {
        ?individual rdf:type ?class .
        FILTER (?class = ns:Person || ?class = ns:Animal)
    }""",
    initNs = {"ns": ns, "rdfs": rdfs})

for r in g.query(q3):
    print(r.individual)

# Ejercicio: 7.4
from rdflib.namespace import FOAF
q4 = prepareQuery("""
    SELECT ?person WHERE {
        ?person foaf:knows ?RockySmith .
        ?person rdf:type ns:Person .
    }""",
    initNs = {"ns": ns, "foaf": FOAF, "rdf": rdf})

for r in g.query(q4):
    print(r.person)

# Ejercicio: 7.5
q5 = prepareQuery("""
    SELECT ?animal WHERE {
        ?animal foaf:knows ?Animal2 .
        ?animal rdf:type ns:Animal .
        ?animal2 rdf:type ns:Animal . 
    }""",
    initNs = {"ns": ns, "foaf": FOAF, "rdf": rdf})

for r in g.query(q5):
    print(r.animal)

# Ejercicio: 7.6
q6 = prepareQuery("""
    SELECT ?livingThing ?age WHERE {
        ?class rdfs:subClassOf* ns:LivingThing .
        ?livingThing rdf:type ?class .
        ?livingThing foaf:age ?age . 
    }
    ORDER BY DESC(?age)
    """,
    initNs = {"rdf": rdf, "foaf": FOAF, "rdfs": rdfs, "ns": ns})

for r in g.query(q6):
    print(r.livingThing, r.age)
    