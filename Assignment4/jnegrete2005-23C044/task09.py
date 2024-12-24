# %% [markdown]
# **Task 09: Data linking**

# %%
from rdflib.plugins.sparql import prepareQuery
from rdflib.namespace import RDF, OWL
from rdflib import Graph, Namespace, Literal, URIRef
%pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2024-2025/master/Assignment4/course_materials/"

# %%
g1 = Graph()
g2 = Graph()
g3 = Graph()
g1.parse(github_storage+"rdf/data03.rdf", format="xml")
g2.parse(github_storage+"rdf/data04.rdf", format="xml")

# %% [markdown]
# Busca individuos en los dos grafos y enlázalos mediante la propiedad OWL:sameAs, inserta estas coincidencias en g3. Consideramos dos individuos iguales si tienen el mismo apodo y nombre de familia. Ten en cuenta que las URI no tienen por qué ser iguales para un mismo individuo en los dos grafos.

# %%
# Bind namespaces


vcard = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")

initNs = {
    "rdf": RDF,
    "owl": OWL,
    "vcard": vcard
}

for prefix, namespace in initNs.items():
    g1.namespace_manager.bind(prefix, namespace, False)
    g2.namespace_manager.bind(prefix, namespace, False)
    g3.namespace_manager.bind(prefix, namespace, False)

# %% [markdown]
# Buscar individuos

# %%
q1 = prepareQuery(
    """
  SELECT ?s1 ?given1 ?family1 WHERE {
    ?s1 vcard:Given ?given1 .
    ?s1 vcard:Family ?family1 .
  } ORDER BY ASC(?family1)
  """,
    initNs
)

q1 = g1.query(q1)

q2 = prepareQuery(
    """
  SELECT ?s2 ?given2 ?family2 WHERE {
    ?s2 vcard:Given ?given2 .
    ?s2 vcard:Family ?family2 .
  } ORDER BY ASC(?family2)
  """,
    initNs
)

q2 = g2.query(q2)

# %% [markdown]
# Enlazar individuos

# %%
g_combined = g1 + g2

q3 = prepareQuery(
    """
  SELECT ?s1 ?s2 WHERE {
    ?s1 vcard:Given ?given .
    ?s1 vcard:Family ?family .
    ?s2 vcard:Given ?given .
    ?s2 vcard:Family ?family .
    FILTER (?s1 != ?s2)
  }
  """,
    initNs
)

for r in g_combined.query(q3):
    g3.add((r.s1, OWL.sameAs, r.s2))

# %% [markdown]
# Visualize results

# %%
print(g3.serialize(format="ttl"))

# %% [markdown]
# Notice that Harry Potter and John Smith are the same person in both graphs, but do not appear in g3. This is because in g1, John has a given of John and in g2 he has a given of Jonathan. On the other hand, in g1 Harry does not have a family name.
# Therefore, as per the criteria, they are not the same person.

# %%
