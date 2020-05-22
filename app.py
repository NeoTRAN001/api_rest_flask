from flask import Flask, jsonify, request
from products import products

app = Flask(__name__)

# Get Data
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify({"products": products})

# Get a Data
@app.route('/products/<string:product_name>', methods=['GET'])
def get_product_name(product_name):
    products_found = [product for product in products if product['name'] == product_name]

    if len(products_found) > 0:
        return jsonify({"product": products_found[0]})

    return jsonify({"message": "Product not found"})

# Insert Data
@app.route('/products', methods=['POST'])
def add_product():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }

    products.append(new_product)
    return jsonify({"message": "Product Added Succesfully", "products": products})

# Update Data Route
@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        productsFound[0]['name'] = request.json['name']
        productsFound[0]['price'] = request.json['price']
        productsFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            'message': 'Product Updated',
            'product': productsFound[0]
        })
    return jsonify({'message': 'Product Not found'})

# DELETE Data Route
@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if len(productsFound) > 0:
        products.remove(productsFound[0])
        return jsonify({
            'message': 'Product Deleted',
            'products': products
        })

def main():
    app.run(debug=True, port=8080)

if __name__ == '__main__':
    main()