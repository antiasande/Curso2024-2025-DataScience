# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CElvA_ZjVxsO0HYOSA5OiXAPog7hlMCj

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

from rdflib.plugins.sparql import prepareQuery
ns = Namespace("http://somewhere#")
q1 = prepareQuery('''
  SELECT ?subclase WHERE {
    ?subclase rdfs:subClassOf ?LivingThing.
  }
  ''',
  initNs = { "rdfs": RDFS, "ns": ns}
)

for r in g.query(q1):
  print(r)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

q2 = prepareQuery('''
  SELECT DISTINCT ?persona WHERE {
    ?Class rdfs:subClassOf* ns:Person .
    ?persona rdf:type ?Class .
    }
  ''',
  initNs = { "rdfs": RDFS, "rdf": RDF, "ns" : ns}
)

for r in g.query(q2):
  print(r)

"""**TASK 7.3: List all individuals of just "Person" or "Animal". You do not need to list the individuals of the subclasses of person (in SPARQL only)**

"""

q3 = prepareQuery('''
  SELECT ?persona WHERE {
    ?subclase rdfs:subClassOf ns:LivingThing.
    ?persona rdf:type ?subclase .
    }
  ''',
  initNs = { "rdfs": RDFS, "rdf": RDF, "ns" : ns}
)

for r in g.query(q3):
  print(r)

"""**TASK 7.4:  List the name of the persons who know Rocky (in SPARQL only)**"""

from rdflib.namespace import FOAF

g.namespace_manager.bind('foaf', FOAF, override=False)
foaf = Namespace("http://xmlns.com/foaf/0.1/")
q4 = prepareQuery('''
    SELECT ?persona WHERE {
        ?persona foaf:knows ns:RockySmith.
    }
    ''',
    initNs={"foaf": FOAF, "ns": ns}
)

for r in g.query(q4):
  print(r)

"""**Task 7.5: List the name of those animals who know at least another animal in the graph (in SPARQL only)**"""

q5 = prepareQuery('''
    SELECT ?animal WHERE {
        ?animal rdf:type ns:Animal.
        ?animal foaf:knows ?animal2.
        ?animal2 rdf:type ns:Animal.
    }
    ''',
    initNs={"rdf": RDF, "foaf": FOAF, "ns": ns}
)

for r in g.query(q5):
  print(r)

"""**Task 7.6: List the age of all living things in descending order (in SPARQL only)**"""

q6 = prepareQuery('''
    SELECT ?livingThing ?age WHERE {
        {
            ?livingThing rdf:type ns:Person.
            ?livingThing foaf:age ?age.
        }
        UNION
        {
            ?livingThing rdf:type ns:Animal.
            ?livingThing foaf:age ?age.
        }
    }
    ORDER BY DESC(?age)
   ''',
   initNs={"rdf": RDF, "foaf": FOAF, "ns": ns}
)

for r in g.query(q6):
  print(r)