from flask import jsonify
from flask_restful import Resource, request
import random

from calificacion_models import input_model, item_model, item_model_result

from sentimental_model import SentimentalModel

class CalificacionResource(Resource):
    
    def __init__(self, model):
        self.model=model
        super(CalificacionResource, self).__init__()
        self.__name__ = "CalificacionResource"  # Agrega el atributo __name__
        
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

        """"
        calificaciones = []
        
        for item in data:
            calificacion = {
                "id": item["id"],
                "mensaje": item["mensaje"],
                "calificacion": self.calcular_puntaje(item["mensaje"])
            }
            calificaciones.append(calificacion)
        """

        new_texts=[]
        calificaciones_id=[]
        for text in data:
            new_texts.append(text['mensaje'])
            calificaciones_id.append({
                "id": text["id"],
                "mensaje": text["mensaje"],
                "calificacion": 0
            })

        calificaciones=self.model.Evaluar(new_texts)
        
        for item,idtext in zip(calificaciones,calificaciones_id):
            idtext["calificacion"]=f"{item['calificacion']}"
            print(f"{item['calificacion']}")

        return jsonify(calificaciones_id)
    
    def calcular_puntaje(self, mensaje):
        return random.randint(1, 5)
