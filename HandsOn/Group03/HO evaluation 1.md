3
    Analysis
    Ontology
        - Even if multiple datasets are used, the domain name (of the ontology and of the data) must be the same. Do not use londonhousing and londonschool.
        - In OWL, there are object properties (where value of the property is a resource) and datatype properties (where the value of the property is a string literal, usually typed). 
        - You are creating classes for the values of datatype properties. However the values of datatype properties are related to datatypes, not classes.
    RDF data
        - Some entities could be encoded as instances and not strings.
            You will need them for linking.
            For example, the towns.
        - The RDF file does not use correctly the classes and properties defined in the ontology. E.g., linkTowns.
    Take into account that the review has been performed over a previous version of the hands-on. Some of the defects found may have been already fixed.
