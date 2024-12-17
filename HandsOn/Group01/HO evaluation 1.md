1
    Analysis
        - The resource naming strategy should use different paths for ontology resources and individuals.
        Also, the #, if present, should be just before the identifier.
    Ontology
        - The ontology does not follow the resource naming strategy defined in the analysis.
        - The rdfs:Class class should not be defined in the ontology.
        - Check that all class names start with capital letter.
        - In OWL, having multiple domains (or ranges) means that the domain (or range) is the intersection of all the classes.  The current definitions of properties with multiple domains are wrong.
        - The domain and/or range of some property is not defined.
    RDF data
        - You don't need to create extra IDs, since the URIs are identifiers.
        - Some individuals have no type.
    Take into account that the review has been performed over a previous version of the hands-on. Some of the defects found may have been already fixed.
