from pymongo import MongoClient

#Conexion Atlas AWS
class conexion:
    def conect():
        client = MongoClient("mongodb+srv://yeison:disPasswordn@distribucion.xbbj9.mongodb.net/distribucion?retryWrites=true&w=majority")
        db = client['disData']
        return db
