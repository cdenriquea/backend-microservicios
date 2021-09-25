from flask import jsonify, request, Response
from db.mongodb import db
from bson import json_util


class crearConductor:
    def write():
        # recibir datos
        nombre = request.json['nombre']
        vehiculo = request.json['vehiculo']
        placa = request.json['placa']
        if nombre and vehiculo and placa:
            id = db.conductores.insert_one(
                {'vehiculo': vehiculo, 'nombre': nombre, 'fecha': nombre}
            )
            response = {
                'id': str(id),
                'vehiculo': vehiculo, 'nombre': nombre, 'fecha': nombre
            }
            return response
        else:
            {'mensaje': 'Faltan datos'}

    def actualizar():
        conductor = request.json['conductor']
        disponibles = db.conductores.update({"nombre": conductor},
                                            {"$set": {"estado": "2"}}, upsert=True)
        response = json_util.dumps(disponibles)

        return Response(response, mimetype='application/json')


class listarConductores:
    def read():
        myquery = {"estado": {"$ne": 2}}
        pedidos = db.conductores.find(myquery)
        response = json_util.dumps(pedidos)

        return Response(response, mimetype='application/json')

    def read2():
        myquery = {"estado": {"$eq": 2}}
        pedidos = db.conductores.find(myquery)
        response = json_util.dumps(pedidos)

        return Response(response, mimetype='application/json')

    def asignar_pedido(lat, lon, cliente):
        disponibles = db.conductores.update({"estado": 0},
                                            {"$set": {"estado": "1", "lon": lon, "latitud": lat, "cliente": cliente}}, upsert=True)
        response = json_util.dumps(disponibles)

        return Response(response, mimetype='application/json')
