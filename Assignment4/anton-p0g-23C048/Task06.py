#!/usr/bin/env python
# coding: utf-8

# **Task 06: Modifying RDF(s)**

# In[46]:


get_ipython().system('pip install rdflib')
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2024-2025/master/Assignment4/course_materials"


# Read the RDF file as shown in class

# In[48]:


from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example5.rdf", format="xml")
print(g.serialize(format="ttl"))


# Create a new class named Researcher

# In[49]:


ns = Namespace("http://somewhere#")
g.add((ns.Researcher, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)


# **TASK 6.1: Create a new class named "University"**
# 

# In[50]:


# TO DO
g.add((ns.University, RDF.type, RDFS.Class))
# Visualize the results
for s, p, o in g:
  print(s,p,o)


# **TASK 6.2: Add "Researcher" as a subclass of "Person"**

# In[51]:


# TO DO
g.add((ns.Researcher, RDFS.subClassOf, ns.Person))
# Visualize the results
for s, p, o in g:
  print(s,p,o)


# **TASK 6.3: Create a new individual of Researcher named "Jane Smithers"**

# In[52]:


# TO DO
jane_smithers = ns.JaneSmithers
g.add((jane_smithers, RDF.type, ns.Researcher))
# Visualize the results
for s, p, o in g:
  print(s,p,o)


# **TASK 6.4: Add to the individual JaneSmithers the email address, fullName, given and family names. Use the https://schema.org vocabulary**

# In[53]:


# TO DO
schema = Namespace("https://schema.org/")
g.add((jane_smithers, schema.email, Literal("jane.smithers@gmail.com")))
g.add((jane_smithers, schema.name, Literal("Jane Smithers")))
g.add((jane_smithers, schema.givenName, Literal("Jane")))
g.add((jane_smithers, schema.familyName, Literal("Smithers")))
# Visualize the results
for s, p, o in g.triples((jane_smithers, None, None)):
  print(s,p,o)


# **TASK 6.5: Add UPM as the university where John Smith works. Use the "https://example.org/ namespace**

# In[61]:


# TO DO

example = Namespace("https://example.org/")
g.namespace_manager.bind('example', Namespace(example), override=False)

UPM = example.UPM
john_smith = ns.JohnSmith

g.add((UPM, RDF.type, ns.University))
g.add((john_smith, schema.worksFor, UPM))

# Visualize the results
for s, p, o in g.triples((john_smith, None, None)):
  print(s,p,o)
for s, p, o in g.triples((UPM, None, None)):
  print(s,p,o)


# **Task 6.6: Add that Jown knows Jane using the FOAF vocabulary. Make sure the relationship exists.**

# In[62]:


# TO DO
from rdflib import FOAF

g.add((john_smith, FOAF.knows, jane_smithers))
# Visualize the results
for s, p, o in g.triples((john_smith, FOAF.knows, None)):
    print(s, p, o)


# In[ ]:




