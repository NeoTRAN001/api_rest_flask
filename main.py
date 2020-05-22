from flask import Flask, jsonify, request
from data import users

app = Flask(__name__)

# ********************* Get Data *********************
@app.route('/', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/<int:id_user>', methods=['GET'])
def get_user(id_user):
    return jsonify(
        [ i for i in users if i['id'] == id_user]
    )

# ********************* Insert Data *********************
@app.route('/', methods=['POST'])
def add_user():
    new_user = {
        "id"     : request.json['id'],
        "name"   : request.json['name'],
        "email"  : request.json['email'],
        "status" : request.json['status'] 
    }
    users.append(new_user)
    return jsonify({"message": "Product Added Succesfully", "New Users": users})

# ********************* Delete Data *********************
@app.route('/<int:id_user>', methods=['DELETE'])
def delete_user(id_user):
    obj_user = [ i for i in users if i['id'] == id_user]
    if len(obj_user) > 0:
        users.remove(obj_user[0])
        return jsonify({
            "message": 'Product Deleted',
            'users': users
        })

# ********************* Update Data *********************
@app.route('/<int:id_user>', methods=['PUT'])
def update_user(id_user):
    obj_user = [i for i in users if i['id'] == id_user]

    if len(obj_user) > 0:
        users.remove(obj_user[0])

        obj_user = {
            "id":     request.json['id'],
            "name":   request.json['name'],
            "email":  request.json['email'],
            "status": request.json['status'] 
        }

        users.append(obj_user)

        return jsonify({
            'message': 'Product Updated',
            'users': obj_user
        })

def main():
    app.run(debug=True, port=3000)

if __name__ == '__main__':
    main()