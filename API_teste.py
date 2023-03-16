from flask import Flask, jsonify, request

app = Flask(__name__)

itens = [
    {'id': 1 ,'nome': 'Livro', 'valor': 35 },
    {'id': 2 ,'nome': 'lápis', 'valor': 1 },
    {'id': 3 ,'nome': 'caderno', 'valor': 15},
]

@app.route('/itens', methods=['GET'])
def  consultar_itens():
    return jsonify(itens)

@app.route('/itens/<int:id>', methods=['GET'])
def obter_por_id(id):
    for iten in itens:
        if iten.get('id') == id:
            return jsonify(iten) 

# editar
@app.route('/itens/<int:id>', methods=['PUT'])
def editar_itens(id):
    iten_alterado = request.get_json()# recebendo informação do usuário
    for indice,intens in enumerate(intens):
        intens[indice].update(iten_alterado)
        return jsonify(intens[indice])

# excluir


app.run(port=5000,host='localhost',debug=True)