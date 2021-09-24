from flask import jsonify, request, Response
from db.mongodb import conexion
from bson import json_util


class generarPedido:
    def write():
        con = conexion
        #recibir datos
        cliente = request.json['cliente']
        documento = request.json['documento']
        fecha = request.json['fecha']
        producto = request.json['producto']
        cantidad = request.json['cantidad']
        pais = request.json['pais']
        departamento = request.json['departamento']
        ciudad = request.json['ciudad']
        direccion = request.json['direccion']
        if cliente and producto and direccion:
            id= con.pedidos.insert_one(
                {'cliente': cliente,'documento':documento,'fecha':fecha,'cantidad': cantidad,'pais':pais,
                'direccion':direccion,'departamento':departamento, 'ciudad': ciudad}
            )
            response = {
                'id':str(id),
                'cliente': cliente,'documento':documento,'fecha':fecha,'cantidad': cantidad,'pais':pais,
                'direccion':direccion,'departamento':departamento, 'ciudad': ciudad
        }
            return response
        else:
            {'mensaje': 'Faltan datos'}

class listarPedidos:
    def read():
        con = conexion
        pedidos = con.pedidos.find()
        response = json_util.dumps(pedidos)

        return Response(response, mimetype = 'application/json')