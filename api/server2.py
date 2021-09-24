from flask import Flask, request
from controllers.pedido import generarPedido, listarPedidos
from controllers.vehiculo import listarConductores, crearConductor

app = Flask(__name__)

##########Pedidos###########
@app.route("/pedido", methods = ['GET'])
def getPedidos():
  return (listarPedidos)


@app.route("/pedido", methods = ['POST'])
def postPedido():
  return (generarPedido)

###########Conductores##########
@app.route("/conductores", methods = ['GET'])
def getConductores():
  return (listarConductores)

@app.route("/conductores", methods = ['POST'])
def postConductor():
  return (crearConductor)


if __name__ == "__main__":
  app.run(host = '0.0.0.0',port=5000, debug= True)
    
