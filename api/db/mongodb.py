from pymongo import MongoClient

# Conexion Atlas AWS

client = MongoClient(
    "mongodb+srv://yeison:disPassword@distribucion.xbbj9.mongodb.net/distribucion?retryWrites=true&w=majority")
db = client['disData']
