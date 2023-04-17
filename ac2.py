from flask import Flask
import json

app = Flask(__name__)

pais = [
    {
        'id': 1,
        'name': "Mexico",
        "description": "No Mexico falamos espanhol"
    },
    {
        "id": 2,
        "name": "Brasil",
        "description": "Aqui é Br"
    },
    {
        "id": 3,
        "name": "Italia",
        "description": "Comemos Pizaa"
    },{
        "id": 4,
        "name": "França",
        "description": "Comemos Pao"
    },
]

paisJSON = json.dumps(pais)


@app.route('/')
def home():
    return "paises"


@app.route('/api/pais', methods=["GET"])
def consultar():
    return paisJSON, 'status code custom'


if __name__ == '__main__':
    app.run()