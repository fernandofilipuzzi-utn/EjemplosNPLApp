# Ejemplo de aplicación utilizando procesamiento de lenguaje natural.

Descripción
Una aplicación de la utilización de modelo sentimentales sería tomar un listado de opiniones y darles una puntuación. Por ejemplo, podrían ser opiniones de películas, compra de productos, etc.
Este ejemplo consiste en montar el modelo en un api rest y consumir dicha api mediante una aplicación desktop, desde esta aplicación se pasan una lista de opciones y la api devuelve la puntuación de dichas opciones.

**server_webapi** 

servicio api rest python que corre el modelo<br/>
* app_fine_tunning.py: toma el dataset y realiza el finetunning
* app_test_fine_tunning.py: prueba el modelo
* app_rest_api.py: corre el servicio

**ClientAPIWeb**

cliente c#  API rest que consume la api.<br/>

**EdicionDataSet**

Sirve para armar el dataset


