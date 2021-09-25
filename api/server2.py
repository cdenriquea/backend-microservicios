from flask import Flask, request
from controllers.pedido import generarPedido, listarPedidos
from controllers.vehiculo import listarConductores, crearConductor
from db.mongodb import db
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)


##########Pedidos###########
@app.route("/pedido", methods=['GET'])
def getPedidos():
    return (listarPedidos.read())


@app.route("/pedido", methods=['POST'])
def postPedido():
    pedido = generarPedido.write()
    listarConductores.asignar_pedido(
        '-75.57081232805264', '6.2367464348557045', pedido['cliente'])
    return (pedido)

###########Conductores##########


@app.route("/conductores", methods=['GET'])
def getConductores():
    return (listarConductores.read())


@app.route("/conductores2", methods=['GET'])
def getConductores2():
    return (listarConductores.read2())


@app.route("/conductores", methods=['POST'])
def postConductor():
    return (crearConductor.write())


@app.route("/actualizar", methods=['PUT'])
def postConductor2():
    response = crearConductor.actualizar()
    return (response)


app.run(host='0.0.0.0', port=5000, debug=True)
