from flask import Flask, jsonify, request
import json


with open("json.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)

app = Flask(__name__)


@app.route('/data')
def obter_contatos():
    return jsonify(dados)




app.run(port=5000,host='localhost',debug=True)