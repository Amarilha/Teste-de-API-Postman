from flask import Flask, jsonify, request

app = Flask(__name__)

itens = [
    {'id': 1 ,'nome': 'Livro', 'valor': 35 },
    {'id': 2 ,'nome': 'lápis', 'valor': 1 },
    {'id': 3 ,'nome': 'caderno', 'valor': 15},
]
# Consultar
@app.route('/itens', methods=['GET'])
def  consultar_itens():
    return jsonify(itens)

# Consultar(id)
@app.route('/itens/<int:id>', methods=['GET'])
def obter_por_id(id):
    for item in itens:
        if item.get('id') == id:
            return jsonify(item) 

# editar
@app.route('/itens/<int:id>', methods=['PUT'])
def editar_itens(id):
    item_alterado = request.get_json()# recebendo informação do usuário
    for indice,item in enumerate(itens):
        if item.get('id') == id:
            itens[indice].update(item_alterado)
            return jsonify(itens[indice])
# criar
@app.route('/itens', methods=['POST'])
def incluir_novo_iten():
    novo_item = request.get_json()
    itens.append(novo_item)

    return jsonify(itens)

# excluir
@app.route('/itens/<int:id>', methods=['DELETE'])
def excluir_itens(id):
    for indice, item in enumerate(itens):
        if item.get('id') == id:
            del itens[indice]

    return jsonify(itens)



app.run(port=5000,host='localhost',debug=True)