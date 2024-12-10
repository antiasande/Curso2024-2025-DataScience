# Hands-on assignment 5 – Self assessment

## Checklist

**Every RDF file:**

- [X] Has at least one owl:sameAs property that links to another dataset

## Comments on the self-assessment
Nuestro RDF usa URIs del estilo "http://example.org/distritos/CiudadLineal" para identificar distritos y barrios. A la hora de reconciliarlo, en el CSV pasó de estar como "CiudadLineal" a "Ciudad Lineal". Eso afecta a cómo se construyen las URIs, ya que con el espacio la URI sería "http://example.org/distritos/Ciudad%20Lineal". Con lo cual, en OpenRefine, una vez obtenidos las URIs de Wikidata asociadas a cada elemento, hemos deshecho la reconciliación en las columnas de distritos y barrios para que no afecte a las URIs.
