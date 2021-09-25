from flask import jsonify, request, Response
from db.mongodb import db
from bson import json_util


class crearConductor:
    def write():
        #recibir datos
        nombre = request.json['nombre']
        vehiculo = request.json['vehiculo']
        placa = request.json['placa']
        if nombre and vehiculo and placa:
            id= db.conductores.insert_one(
                {'vehiculo': vehiculo,'nombre':nombre,'fecha':nombre}
            )
            response = {
                'id':str(id),
                'vehiculo': vehiculo,'nombre':nombre,'fecha':nombre
        }
            return response
        else:
            {'mensaje': 'Faltan datos'}

class listarConductores:
    def read():
        pedidos = db.conductores.find()
        response = json_util.dumps(pedidos)

        return Response(response, mimetype = 'application/json')