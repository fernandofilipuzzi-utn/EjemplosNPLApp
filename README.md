# Ejemplo de aplicación utilizando procesamiento de lenguaje natural.

## Descripción
Una aplicación de la utilización de modelo sentimentales sería tomar un listado de opiniones y darles una puntuación. Por ejemplo, podrían ser opiniones de películas, compra de productos, etc.
Este ejemplo consiste en montar el modelo en un api rest y consumir dicha api mediante una aplicación desktop, desde esta aplicación se pasan una lista de opciones y la api devuelve la puntuación de dichas opciones.

Hay tres aplicaciones:

**<a href="https://github.com/fernandofilipuzzi-utn/EjemplosNPLApp/tree/main/SentimentalAppNPL/server_webapi">server_webapi</a>** 

Es servicio API rest python <b>9.11</b> que corre el modelo<br/>

* app_fine_tunning.py: toma el dataset y realiza el finetunning
* app_test_fine_tunning.py: prueba el modelo
* app_rest_api.py: corre el servicio

```bash
mkdir .venv
pipenv shell
pipenv install
```

luego, para la sintonía fina:

```bash
python app_fine_tunning.py
```

seguido, se puede probar si todo está correcto con:

```bash
python app_test_fine_tunning.py
```

finalmente, cambiar la ip en app_rest_api.py y correr con:

```bash
python app_rest_api.py
```

Para consultar la API lanzada, desde el navegador la url sería: <br>http://<b>ip_configurada</b>:5000/swagger


**<a href="https://github.com/fernandofilipuzzi-utn/EjemplosNPLApp/tree/main/SentimentalAppNPL/ClientAPIWeb">ClientAPIWeb</a>**

Es el cliente c# API rest ejemplo que consume la API.<br/>

**<a href="https://github.com/fernandofilipuzzi-utn/EjemplosNPLApp/tree/main/SentimentalAppNPL/EdicionDataSet">EdicionDataSet</a>**

Sirve para armar el dataset que consiste en un archivo con un objeto json: Ejemplo actual: <a href="https://github.com/fernandofilipuzzi-utn/EjemplosNPLApp/blob/main/SentimentalAppNPL/server_webapi/dataset/input.json">input.json</a>

