from flask import Flask, request, jsonify

app = Flask(__name__)

products = []


@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)


@app.route('/products/<string:name>', methods=['GET'])
def get_product(name):
    for product in products:
        if product['name'] == name:
            return jsonify(product)
    return jsonify({'message': 'Product not found'})


@app.route('/products', methods=['POST'])
def create_product():
    new_product = {
        'name': request.json['name'],
        'price': request.json['price']
    }
    products.append(new_product)
    return jsonify(new_product), 201


@app.route('/products/<string:name>', methods=['PUT'])
def update_product(name):
    for product in products:
        if product['name'] == name:
            product['price'] = request.json['price']
            return jsonify(product)
    return jsonify({'message': 'Product not found'})


@app.route('/products/<string:name>', methods=['DELETE'])
def delete_product(name):
    for product in products:
        if product['name'] == name:
            products.remove(product)
            return jsonify({'message': 'Product deleted'})
    return jsonify({'message': 'Product not found'})


if __name__ == '__main__':
    app.run()
