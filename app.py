from flask import Flask, jsonify, request
import json


with open("json.json", encoding='utf-8') as json_file:
    data = json.load(json_file)

app = Flask(__name__)


@app.route('/data',methods=['GET'])
def contatos():
    return jsonify(data)

@app.route('/datapost',methods=['POST'])
def add_register():
    new_register = request.get_json()
    data.append(new_register)
    return data


app.run(port=5000,host='localhost',debug=True)