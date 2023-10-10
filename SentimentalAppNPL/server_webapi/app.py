#app.py

from flask import Flask
from flasgger import Swagger
from flask_restful import Api

from calificacion_resource import CalificacionResource
from sentimental_model import SentimentalModel

app = Flask(__name__)
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "swagger",
            "route": "/swagger.json",
            "rule_filter": lambda rule: True,  # Mostrar todas las reglas
            "model_filter": lambda tag: True,  # Mostrar todos los modelos
        }
    ],
    "static_url_path": "/flasgger_static",  # Ruta para los archivos estáticos de Swagger UI
    "swagger_ui": True,  # Habilitar el UI de Swagger
    "specs_route": "/swagger/"  # Ruta para el UI de Swagger
}

Swagger(app, config=swagger_config)
api = Api(app)

model=SentimentalModel()

calificacion_resource=CalificacionResource(model)

#api.add_resource(calificacion_resource, '/calificaciones')
api.add_resource(CalificacionResource, '/calificaciones', resource_class_kwargs={'model': model})

if __name__ == '__main__':
    app.run(debug=True, host='192.168.1.186', port=5000)
#    app.run(debug=True, host='0.0.0.0', port=5000)