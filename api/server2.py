from flask import Flask, request
from controllers.pedido import generarPedidos, listarPedidos

app = Flask(__name__)


@app.route("/pedido", methods = ['GET'])
def getAll():
  return (listarPedidos)

@app.route("/pedido", methods = ['POST'])
def postOne():
  return (generarPedidos)


if __name__ == "__main__":
  app.run(host = '0.0.0.0',port=5000, debug= True)
    
