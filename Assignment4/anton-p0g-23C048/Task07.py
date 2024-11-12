#!/usr/bin/env python
# coding: utf-8

# **Task 07: Querying RDF(s)**

# In[1]:


get_ipython().system('pip install rdflib')
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2024-2025/master/Assignment4/course_materials"


# First let's read the RDF file

# In[2]:


from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")


# **TASK 7.1: List all subclasses of "LivingThing" with RDFLib and SPARQL**

# In[40]:


# TO DO
from rdflib.plugins.sparql import prepareQuery
ns = Namespace("http://somewhere#")

q1 = prepareQuery('''
    SELECT ?subclass
    WHERE {
        ?subclass rdfs:subClassOf ns:LivingThing
    }
    ''', 
    initNs = {"rdfs": RDFS, "ns": Namespace("http://somewhere#")})

# Visualize the results
print("Using SPAQL:")
for r in g.query(q1):
    print(r)

print("\nUsing RDFLib:")
for s, p, o in g.triples((None, RDFS.subClassOf, ns.LivingThing)):
    print(s)


# **TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**
# 

# In[39]:


# TO DO
q2 = prepareQuery('''
    SELECT ?individual
    WHERE {
        ?individual rdf:type ns:Person
    }
    ''', 
    initNs = {"rdfs": RDFS, "ns": Namespace("http://somewhere#")})

# Visualize the results
print("Using SPAQL:")
for r in g.query(q2):
    print(r)

print("\nUsing RDFLib:")
for s, p, o in g.triples((None, RDF.type, ns.Person)):
    print(s)


# **TASK 7.3: List all individuals of just "Person" or "Animal". You do not need to list the individuals of the subclasses of person (in SPARQL only)**
# 

# In[51]:


# TO DO
q3 = prepareQuery('''
    SELECT ?individual
    WHERE 
    {
        {
            ?individual a ns:Person .
            FILTER NOT EXISTS {
                ?individual a ?subclass .
                ?subclass rdfs:subClassOf ns:Person
            }
        }
        UNION
        {
            ?individual a ns:Animal .
            FILTER NOT EXISTS {
                ?individual a ?subclass .
                ?subclass rdfs:subClassOf ns:Animal
            }
        }
    }
    ''', 
    initNs={"ns": Namespace("http://somewhere#"), "rdfs": RDFS})

# Visualize the results
for r in g.query(q3):
    print(r)


# **TASK 7.4:  List the name of the persons who know Rocky (in SPARQL only)**

# In[70]:


# TO DO
q4 = prepareQuery(
    '''
    SELECT ?person_name
    WHERE {
        ?person_name foaf:knows ns:RockySmith
    }
    ''', 
    initNs={"ns": Namespace("http://somewhere#"), 
            "foaf": Namespace("http://xmlns.com/foaf/0.1/")})

# Visualize the results
for r in g.query(q4):
    print(r)


# **Task 7.5: List the name of those animals who know at least another animal in the graph (in SPARQL only)**

# In[76]:


# TO DO
q5 = prepareQuery(
    '''
    SELECT ?animal
    WHERE {
        ?animal a ns:Animal .
        ?animal foaf:knows ?other_animal .
        ?other_animal a ns:Animal .
    }
    ''', 
    initNs={"ns": Namespace("http://somewhere#"), 
            "foaf": Namespace("http://xmlns.com/foaf/0.1/")})

# Visualize the results
for r in g.query(q5):
    print(r)


# **Task 7.6: List the age of all living things in descending order (in SPARQL only)**

# In[82]:


# TO DO
q6 = prepareQuery(
    '''
    SELECT ?livingThing ?age
    WHERE {
        {
            ?livingThing a ns:Person .
            ?livingThing foaf:age ?age .
        }
        UNION
        {
            ?livingThing a ns:Animal .
            ?livingThing foaf:age ?age .
        }
    }
    ORDER BY DESC(?age)
    ''', 
    initNs={"ns": Namespace("http://somewhere#"), 
            "foaf": Namespace("http://xmlns.com/foaf/0.1/")})

# Visualize the results
for r in g.query(q6):
    print(r)

