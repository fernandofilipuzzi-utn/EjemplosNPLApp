from flask import jsonify
from flask_restful import Resource, request
import random

from models.calificacion_models import input_model, item_model, item_model_result

from models.sentimental_model import SentimentalModel

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
            example: [{"id":"1", "comentario":"la película fue buenísima"},{"id":"2", "comentario":"estuvo regular."}]
            schematic:
              type: array
              items:
                petType: item_model

        responses:
          200:
            description: Lista de usuarios en formato JSON.
        """
        data = request.get_json()

        new_texts=[]
        valoraciones_id=[]
        for text in data:
            new_texts.append(text['comentario'])
            valoraciones_id.append({
                "id": text["id"],
                "comentario": text["comentario"],
                "valoracion": 0
            })

        valoraciones=self.model.Evaluar(new_texts)
        
        for item,idtext in zip(valoraciones,valoraciones_id):
            idtext["valoracion"]=f"{item['valoracion']}"
            print(f"{item['valoracion']}")

        return jsonify(valoraciones_id)
    
    def calcular_puntaje(self, mensaje):
        return random.randint(1, 5)
