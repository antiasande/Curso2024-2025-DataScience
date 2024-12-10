6
    Analysis
        The URIs of the ontology terms do not have to end with # (ontology/Accidente#); the hash is placed before (ontology#Accidente).
    Ontology
        - The ontology presents serialization issues; is not a valid Turtle file.
            ("ns: OcurreEn")
    RDF data
        - Accidents are mixing the information about persons.
        - Date values are not encoded properly.
        - Datatypes are missing.
        - Addresses are typed as accidents.
        - Review the way in which you define URIs. The URI of a location should not depend on the accidents taking place there.
    Take into account that the review has been performed over a previous version of the hands-on. Some of the defects found may have been already fixed.
