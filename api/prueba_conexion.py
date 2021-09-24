from flask import Flask
from pymongo import MongoClient
app = Flask(__name__)


try:
  mongo = MongoClient("mongodb+srv://yeison:disPassword@distribucion.xbbj9.mongodb.net/disData?retryWrites=true&w=majority")
  db =mongo.company
  mongo.server_info() #Mirar excepcion si no se puede conectar a mongo
except:
  print('*****************************')
  print('Error de conexion a Mongo')
  print('*****************************')

#############################################
@app.route("/users", methods = ['POST'])
def create_user():
  user = {"name":"A","lastName":"AA"}
  dbResponse = db.users.insert_one(user)
  print(dbResponse.inserted_id)
  return "x"
#############################################

if __name__ == "__main__":
  app.run(port=80, debug= True)