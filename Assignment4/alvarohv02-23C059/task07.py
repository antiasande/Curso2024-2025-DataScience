# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bv9JEFTRxTgVLdAc2u2BVxKKmnoxRhWL

**Task 07: Querying RDF(s)**
"""

!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2024-2025/master/Assignment4/course_materials"

"""First let's read the RDF file"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

"""**TASK 7.1: List all subclasses of "LivingThing" with RDFLib and SPARQL**"""

# TO DO
# Visualize the results

from rdflib.plugins.sparql import prepareQuery
ns = Namespace("http://somewhere#")
rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
q1 = prepareQuery('''
  SELECT ?subclass WHERE {
    ?subclass rdfs:subClassOf* ns:LivingThing .
    }''',
  initNs = {"ns": ns, "rdfs": rdfs})

for r in g.query(q1):
  print(r)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

# TO DO

q1 = prepareQuery('''
  SELECT ?individuals WHERE {
    ?individuals rdf:type/rdfs::subClass* ns:Person .
  }
''',
initNs= {"rdfs":rdfs, "ns":ns}
)
# Visualize the results
for r in g.query(q1):
  print(r)

"""**TASK 7.3: List all individuals of just "Person" or "Animal". You do not need to list the individuals of the subclasses of person (in SPARQL only)**

"""

# TO DO
# Visualize the results
from rdflib.namespace import FOAF, RDF

query = """
    SELECT ?individual
    WHERE {
        ?individual rdf:type ?type .
        FILTER (?type = foaf:Person || ?type = ns:Animal)
    }
"""

q1 = prepareQuery(query, {"foaf":FOAF, "rdf":RDF, "ns":ns})

for r in g.query(q1):
  print(r)

"""**TASK 7.4:  List the name of the persons who know Rocky (in SPARQL only)**"""

# TO DO
# Visualize the results

query = """
SELECT ?name
WHERE {
    ?person rdf:type foaf:Person .
    ?person foaf:knows ns:Rocky .
    ?person foaf:name ?name .
}"""

q1 = prepareQuery(query, {"ns":ns, "foaf":FOAF})

for r in g.query(q1):
  print(r)

"""**Task 7.5: List the name of those animals who know at least another animal in the graph (in SPARQL only)**"""

# TO DO
# Visualize the results


query = """SELECT DISTINCT ?animal
WHERE {
    ?animal foaf:knows ?otherAnimal .
    ?otherAnimal a ns:Animal .
}
"""

q1 = prepareQuery(query, {"ns":ns, "foaf":FOAF})
for r in g.query(q1):
  print(r)

"""**Task 7.6: List the age of all living things in descending order (in SPARQL only)**"""

# TO DO
# Visualize the results

query ="""
SELECT ?livingThing ?age
WHERE {
    ?livingThing a ns:LivingThing .
    ?livingThing rdf:hasAge ?age .
}
ORDER BY DESC(?age)
"""

q1 = prepareQuery(query, {"ns":ns, "rdf":RDF})