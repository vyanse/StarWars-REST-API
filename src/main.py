"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@app.route('/people',methods=['GET'])
def get_people():
    # consultar todos los personajes
    # devolver personas serializadas 
    return 'personas consultadas', 200

@app.route('/people/<int:people_id>', methods=['GET'])
def get_person(people_id):
    person = 'el query que hicimos de las personas'
    # consultar un id especifico y guardar esa informacion en la variable person
    # mostrar la informacion del id y si no existe, mostrar un error (no se encuentra registrado)
    if person != None:

        return 'info de personas consultadas', 200
    else:
        return 'no se encontro registrado', 404

@app.route('/planets', methods=['GET'])
def get_planet():
    # consultar todos los planetas en DB
    # devolver planetas serializados
    return "Planetas consultados", 200

@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planetid(planet_id):
    
    # consultar todos los planeta individual en DB
    #si no se encuentra devolver alerta de que no se encuentra ese registro
    # devolver planeta serializado
    return "informacion de Planeta consultado", 404



# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
