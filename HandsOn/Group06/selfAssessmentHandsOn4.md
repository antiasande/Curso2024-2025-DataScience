# Hands-on assignment 4 – Self assessment

## Checklist

**Every RDF file:**

- [x] Uses the .nt extension
- [x] Is serialized in the NTriples format
- [x] Follows the resource naming strategy
- [x] Uses class and property URIs that are the same as those used in the ontology

**Every URI in the RDF files:**

- [x] Is "readable" and has some meaning (e.g., it is not an auto-increased integer) 
- [x] Is not encoded as a string
- [x] Does not contain a double slash (i.e., “//”)

**Every individual in the RDF files:**

- [x] Has a label with the name of the individual
- [x] Has a type

**Every value in the RDF files:**

- [x] Is trimmed
- [x] Is properly encoded (e.g., dates, booleans)
- [x] Includes its datatype
- [x] Uses the correct datatype (e.g., values of 0-1 may be booleans and not integers, not every string made of numbers is a number)

## Comments on the self-assessment
## Tareas Realizadas

- 1. Crear el archivo de mapeo RML: Un archivo RML define como debemos mapear las columnas de csv a las tripletas familiares de RDF. Empleando Turtle y siguiendo las plantillas y ejemplos proporcionados en el repositorio de GitHub. 
- 2. La siguiente tarea opcional consiste en crear un archivo YML , lo que hicimos aquí fué definir las reglas adicionales para la configuración del motor de mapeo.
- 3. Por último generamos el RDF, que era nuestro objetivo inicial .

## Evaluación del Desempeño 

- Para crear nuestro archivo RML utilizamos el estándar de Turtle que nos representaría las reglas de manera clara, el archivo lo guardamos con la extensión .rml en el directorio mappings.
- Usamos también para crear el YML el archivo morph_kgc_sample_project proporcionado adaptándolo a las necesidades del dataset, guardando también este archivo en mappings.
- A la hora de generar el RDF , usamos un motor como Morph-KGC , este interpretara las reglas definidas en los archivos .rml y .yml transformando finalmente los datos originales correspondientes al archivo csv en tripletas rdf.

## Conclusión

- A través de esta práctica, hemos conseguido transformar los datos que llevamos modificando y adecuando en las entregas anteriores en formato csv a tripletas RDF mediante una serie de plantillas estructuradas .