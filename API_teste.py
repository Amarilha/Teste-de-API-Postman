form  flask import Flask, jsonify, request

app = Flask(__name__)

itens = [
    {'id': 1 ,'nome': 'Livro', 'valor': 35 }
    {'id': 2 ,'nome': 'lápis', 'valor': 1 }
    {'id': 3 ,'nome': 'caderno', 'valor': 15 }
]

@app.route('/itens')
def  consultar_itens():
    return jsonify(itens)


app.run(port=5000,host='localhost')