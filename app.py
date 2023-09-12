from flask import Flask, jsonify, request
import json


with open("json.json", encoding='utf-8') as json_file:
    data = json.load(json_file)

app = Flask(__name__)


@app.route('/data',methods=['GET'])
def contatos():
    return jsonify(data)

@app.route('/data/<string:id>',methods=['GET'])
def atendimentos_id(id):
    for atendimento in data["Atendimentos"]:
        if atendimento.get('AtendimentoCodigo') == id:
            return jsonify(atendimento)


@app.route('/datapost',methods=['POST'])
def add_register():
    new_register = request.get_json()
    data["Atendimentos"].append(new_register)
    return data


@app.route('/data/<string:id>',methods=['PUT'])
def update_register_id(id):
    update_register = request.get_json()
    for i,atendimento in enumerate(data["Atendimentos"]):
        if atendimento.get('AtendimentoCodigo') == id:
            data["Atendimentos"][i].update(update_register)
            return jsonify(data["Atendimentos"][i])


app.run(port=5000,host='localhost',debug=True)