# Hands-on assignment 2 – Self assessment

## Checklist

### The “analysis.html” file:

- [x] Includes the potential license of the dataset to be generated
- [x] Includes the resource naming strategy

### The resource naming strategy:

- [x] Uses a domain that is not the one given by default in Protégé
- [x] Uses different paths for ontology resources (i.e., classes and properties) and individuals
- [x] Ensures that the paths for individuals of different classes are not the same
- [x] Defines individual URIs independently of class URIs

### The ontology file:

- [x] Uses the .ttl extension
- [x] Is serialized in the Turtle format
- [x] Follows the resource naming strategy
- [x] Contains at least one class.
        El archivo contiene varias clases, como Accidente, Persona, Vehiculo.
- [x] Contains at least one object property (where the value of the property is a resource).
        Tienes varias propiedades de objeto, como involucravehiculo, participapersona
- [x] Contains at least one datatype property (where the value of the property is a string literal, usually typed).
        Hay varias propiedades de datos, como fecha, lugar, tipoAccidente,
- [x] Defines the domain of all the properties (the origin of the property)
- [x] Defines the range of all the properties (the destination of the property)
- [x] Defines all class names starting with a capital letter
- [x] Defines all property names starting with a non-capital letter
- [x] Does not mix labels in different languages (e.g., Spanish and English)
- [x] Does not define multiple domains or multiple ranges in properties
- [x] Contains at least one class that will be used to link to other entities.
        La clase Accidente se usa para enlazar con otras entidades, como vehículos y personas.

## Conclusion
A lo largo del trabajo, se lograron cumplir los requisitos presentados con respecto a la estructura de la ontología, la definición de las clases y propiedades y la aplicación de una estrategia de nombres adecuada.
A veces encontrar nombres coherentes y que sigan las buenas prácticas en ontologías fue complicado.
Las decisiones tomadas respecto a la elección de clases y propiedades fueron necesarias para reflejar las necesidades del dominio de nuestro proyecto, que se basa en los accidentes de tráfico. 
