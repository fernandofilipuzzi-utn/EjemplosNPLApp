from flask import jsonify
from flask_restful import Resource, request
import random

from calificacion_models import input_model, item_model, item_model_result

class CalificacionResource(Resource):
    def post(self):
        """
        post endpoint
        ---
        tags:
          - flast restful apis
        parameters:
          - name: data
            in: body
            description: datos
            required: false
            type: object
            example: [{"id":"1", "mensaje":"hola"},{"id":"1", "mensaje":"hola"}]
            schematic:
              type: array
              items:
                petType: item_model

        responses:
          200:
            description: Lista de usuarios en formato JSON.
        """
        data = request.get_json()

        calificaciones = []

        for item in data:
            calificacion = {
                "id": item["id"],
                "mensaje": item["mensaje"],
                "calificacion": self.calcular_puntaje(item["mensaje"])
            }
            calificaciones.append(calificacion)

        return jsonify(calificaciones)
    
    
    def calcular_puntaje(self, mensaje):
        return random.randint(1, 5)
