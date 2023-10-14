# Ejemplo de aplicación utilizando procesamiento de lenguaje natural.

## Descripción
En este repositorio se aloja una aplicación de la utilización de un modelo de clasificación de sentimientos. El montaje consiste en tomar un listado de opiniones comentarios y darles una puntuación. En este caso se trabajo con una lista de críticas de cine.

Se realizó una API Rest en python que recibe las consultas a valorar y la cual levanta el modelo NPL. También se incluye una aplicación Windows Form en c# que completa la prueba de concepto de la idea de aplicación de este modelo de clasificación de sentimientos.

En el repositorio se encuentran tres aplicaciones:

**1- <a href="https://github.com/fernandofilipuzzi-utn/EjemplosNPLApp/tree/main/SentimentalAppNPL/server_webapi">server_webapi</a>** 

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


**2- <a href="https://github.com/fernandofilipuzzi-utn/EjemplosNPLApp/tree/main/SentimentalAppNPL/ClientAPIWeb">ClientAPIWeb</a>**

Es el cliente c# API rest ejemplo que consume la API.<br/>

**3- <a href="https://github.com/fernandofilipuzzi-utn/EjemplosNPLApp/tree/main/SentimentalAppNPL/EdicionDataSet">EdicionDataSet</a>**

Sirve para armar el dataset que consiste en un archivo con un objeto json: Ejemplo actual: <a href="https://github.com/fernandofilipuzzi-utn/EjemplosNPLApp/blob/main/SentimentalAppNPL/server_webapi/dataset/input.json">input.json</a>

