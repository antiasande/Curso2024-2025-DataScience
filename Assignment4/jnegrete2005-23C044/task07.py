# %% [markdown]
# **Task 07: Querying RDF(s)**

# %%
from rdflib.plugins.sparql import prepareQuery
from rdflib.namespace import RDF, RDFS, FOAF
from rdflib import Graph, Namespace, Literal
%pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2024-2025/master/Assignment4/course_materials"

# %% [markdown]
# First let's read the RDF file

# %%
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.namespace_manager.bind("foaf", Namespace("http://xmlns.com/foaf/spec/"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

# %% [markdown]
# **TASK 7.1: List all subclasses of "LivingThing" with RDFLib and SPARQL**

# %%

NS = Namespace("http://somewhere#")

initNs = {"rdf": RDF, "rdfs": RDFS, "ns": NS, "foaf": FOAF}

q1 = prepareQuery(""" 
  SELECT ?s WHERE {
    ?s rdfs:subClassOf ns:LivingThing .
  }
  """,
                  initNs=initNs
                  )

# Now with RDFLib
for s in g.subjects(RDFS.subClassOf, NS.LivingThing):
    print(s)

print()

# Visualize the results
for r in g.query(q1):
    print(r.s)

# %% [markdown]
# **TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**
#

# %%
q2 = prepareQuery("""
  SELECT ?s WHERE {{              
      ?s rdf:type ns:Person .
    } UNION {
      ?subclass rdfs:subClassOf ns:Person .
      ?s rdf:type ?subclass .
    }
  }
  """,
                  initNs=initNs
                  )

# Now with RDFLib
people = g.subjects(RDF.type, NS.Person)
people = list(people)

# Add the subclasses of Person
for s, _, o in g.triples((None, RDFS.subClassOf, NS.Person)):
    people += list(g.subjects(RDF.type, s))

for p in people:
    print(p)

print()

# Visualize the results
for r in g.query(q2):
    print(r.s)

# %% [markdown]
# **TASK 7.3: List all individuals of just "Person" or "Animal". You do not need to list the individuals of the subclasses of person (in SPARQL only)**
#

# %%
q3 = prepareQuery(
    """ 
  SELECT ?s WHERE {{
      ?s rdf:type ns:Person .
    } UNION {
      ?s rdf:type ns:Animal .
    }
  }
  """,
    initNs=initNs
)

# Visualize the results
for r in g.query(q3):
    print(r.s)

# %% [markdown]
# **TASK 7.4:  List the name of the persons who know Rocky (in SPARQL only)**

# %%
q4 = prepareQuery(
    """
  SELECT ?s WHERE { {
    ?s rdf:type ns:Person .
    ?s foaf:knows ns:RockySmith .
  } UNION {
    ?subclass rdfs:subClassOf ns:Person .
    ?s rdf:type ?subclass .
    ?s foaf:knows ns:RockySmith .
  } }
  """,
    initNs=initNs
)

# Visualize the results
for r in g.query(q4):
    print(r.s)

# %% [markdown]
# **Task 7.5: List the name of those animals who know at least another animal in the graph (in SPARQL only)**

# %%
q5 = prepareQuery(
    """
  SELECT ?s WHERE {
    ?s rdf:type ns:Animal .
    ?other rdf:type ns:Animal .
    ?s foaf:knows ?other .
  }
  """,
    initNs=initNs
)

# Visualize the results
for r in g.query(q5):
    print(r.s)

# %% [markdown]
# **Task 7.6: List the age of all living things in descending order (in SPARQL only)**

# %%
q6 = prepareQuery(
    """
  SELECT ?age WHERE {
    ?subclass rdfs:subClassOf* ns:LivingThing .
    ?s rdf:type ?subclass .
    ?s foaf:age ?age .
  } ORDER BY DESC(?age)
  """,
    initNs=initNs
)

# Visualize the results
for r in g.query(q6):
    print(f"Age: {r.age}")
