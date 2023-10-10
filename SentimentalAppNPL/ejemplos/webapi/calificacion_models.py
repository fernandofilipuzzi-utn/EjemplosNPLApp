#calificacion_models.py
from flask_restful import fields

class ItemModel:
    def __init__(self, id, mensaje):
        self.id = id
        self.mensaje = mensaje

item_model = {
    'id': fields.Integer,
    'mensaje': fields.String
}

class ItemModelResult:
    def __init__(self, id, mensaje, calificacion):
        self.id = id
        self.mensaje = mensaje
        self.calificacion = calificacion

item_model_result = {
    'id': fields.Integer,
    'mensaje': fields.String,
    'calificacion': fields.Integer
}

class InputModel:
    def __init__(self, data):
        self.data = data

input_model = {
    'data': fields.List(fields.Nested(item_model))
}
