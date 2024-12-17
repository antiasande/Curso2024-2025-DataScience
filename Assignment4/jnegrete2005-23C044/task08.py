# %% [markdown]
# **Task 08: Completing missing data**

# %%
from rdflib.namespace import RDF
from rdflib.plugins.sparql import prepareQuery
from rdflib import Graph, Namespace, Literal, URIRef
%pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2024-2025/master/Assignment4/course_materials"

# %%
g1 = Graph()
g2 = Graph()
g1.parse(github_storage+"/rdf/data01.rdf", format="xml")
g2.parse(github_storage+"/rdf/data02.rdf", format="xml")

# %% [markdown]
# Tarea: lista todos los elementos de la clase Person en el primer grafo (data01.rdf) y completa los campos (given name, family name y email) que puedan faltar con los datos del segundo grafo (data02.rdf). Puedes usar consultas SPARQL o iterar el grafo, o ambas cosas.

# %%
# Bind namespaces

VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")
NS = Namespace("http://data.org#")
initNs: dict[str, Namespace] = {
    "vcard": VCARD,
    "rdf": RDF,
    "ns": NS
}

for key in initNs:
    g1.namespace_manager.bind(key, initNs[key], False)
    g2.namespace_manager.bind(key, initNs[key], False)

# %%
# Define a function to format and print the results as a table


def print_table(results):
    # Print the header
    print(f"{'Person':<30} {'Given Name':<20} {'Family Name':<20} {'Email':<30}")
    print("-" * 100)  # A line separator

    # Print each row of results
    for r in results:
        person = str(r.person)
        given = str(r.given) if r.given else "N/A"
        family = str(r.family) if r.family else "N/A"
        email = str(r.email) if r.email else "N/A"

        # Print each field with padding for alignment
        print(f"{person:<30} {given:<20} {family:<20} {email:<30}")

# %% [markdown]
# List all the elements off class Person on g1


# %%
q1 = prepareQuery(
    """
  SELECT ?person ?given ?family ?email WHERE {
    ?person rdf:type ns:Person .
    OPTIONAL { ?person vcard:Given ?given . }
    OPTIONAL { ?person vcard:Family ?family . }
    OPTIONAL { ?person vcard:EMAIL ?email . }
  }
  """,
    initNs
)

q1 = g1.query(q1)
print_table(q1)

# %% [markdown]
# Do the same thing in g2

# %%
q2 = prepareQuery(
    """
  SELECT ?person ?given ?family ?email WHERE {
    ?person rdf:type ns:Person .
    OPTIONAL { ?person vcard:Given ?given . }
    OPTIONAL { ?person vcard:Family ?family . }
    OPTIONAL { ?person vcard:EMAIL ?email . }
  }
  """,
    initNs
)

q2 = g2.query(q2)
print_table(q2)

# %% [markdown]
# Now, complete the missing data in g1 with the data in g2

# %%
# Merge the two graphs
g1 += g2

q = prepareQuery(
    """
  SELECT ?person ?given ?family ?email WHERE {
    ?person rdf:type ns:Person .
    OPTIONAL { ?person vcard:Given ?given . }
    OPTIONAL { ?person vcard:Family ?family . }
    OPTIONAL { ?person vcard:EMAIL ?email . }
  }
  """,
    initNs
)

print_table(g1.query(q))
