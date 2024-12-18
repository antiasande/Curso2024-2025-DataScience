7
    Analysis
        - Very good!
    Ontology
        - The XML Schema datatype xsd:time is not correctly written.
        - The domain and/or range of some property is not defined.
        - In OWL, having multiple domains (or ranges) means that the domain (or range) is the intersection of all the classes.  The current definitions of properties with multiple domains are wrong.
    RDF data
        - The RDF file does not follow the resource naming strategy.
        - Therefore, it could happen that two individuals from different classes have the same URI because the naming strategy does not ensure uniqueness.
        - Identifiers are not numbers.
        - Some values should be represented as booleans.
        - The hasFloorNumber property uses a different namespace.
    Take into account that the review has been performed over a previous version of the hands-on. Some of the defects found may have been already fixed.
