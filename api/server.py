from flask import Flask, request, Response
from bson import json_util
from pymongo import MongoClient
#from flask_cors import CORS

app = Flask(__name__)
#CORS(app)
client = MongoClient("mongodb+srv://yeison:disPassword@distribucion.xbbj9.mongodb.net/distribucion?retryWrites=true&w=majority")
conexion = client['disData']

@app.route("/pedido", methods = ['GET'])
def getAll():
        con = conexion
        pedidos = con.pedidos.find()
        response = json_util.dumps(pedidos)

        return Response(response, mimetype = 'application/json')

@app.route("/pedido", methods = ['POST'])
def postOne():
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

###########Conductores##########
@app.route("/conductores", methods = ['POST'])
def postConductor():
        con = conexion
        #recibir datos
        nombre = request.json['nombre']
        vehiculo = request.json['vehiculo']
        placa = request.json['placa']
        if nombre and vehiculo and placa:
            id= con.conductores.insert_one(
                {'vehiculo': vehiculo,'nombre':nombre,'placa':placa}
            )
            response = {
                'id':str(id),
                'vehiculo': vehiculo,'nombre':nombre,'placa':placa
            }
            return response
        else:
            {'mensaje': 'Faltan datos'}

@app.route("/conductores", methods = ['GET'])
def getConductores():
        con = conexion
        pedidos = con.conductores.find()
        response = json_util.dumps(pedidos)

        return Response(response, mimetype = 'application/json')


if __name__ == "__main__":
  app.run(host = '0.0.0.0',port=5000, debug= True)