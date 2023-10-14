#calificacion_models.py
from flask_restful import fields

class ItemModel:
    def __init__(self, id, mensaje):
        self.id = id
        self.mensaje = mensaje

item_model = {
    'id': fields.Integer,
    'comentario': fields.String,
    'valoracion': fields.Integer
}

class ItemModelResult:
    def __init__(self, id, comentario, valoracion):
        self.id = id
        self.comentario = comentario
        self.valoracion = valoracion

item_model_result = {
    'id': fields.Integer,
    'comentario': fields.String,
    'valoracion': fields.Integer
}

class InputModel:
    def __init__(self, data):
        self.data = data

input_model = {
    'data': fields.List(fields.Nested(item_model))
}
