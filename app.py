from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers import cats
from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({'message': 'Hello from Flask!'}), 200

@app.route('/api/cats', methods=['GET', 'POST'])
def cats_handler():
    fns = {
        'GET': cats.index,
        'POST': cats.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code

@app.route('/api/cats/<int:cat_id>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
def cat_handler(cat_id):
    fns = {
        'GET': cats.show,
        'PATCH': cats.update,
        'PUT': cats.update,
        'DELETE': cats.destroy
    }
    resp, code = fns[request.method](request, cat_id)
    return jsonify(resp), code

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404

@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {'message': f"It's not you, it's us"}, 500

if __name__ == "__main__":
    app.run(debug=True)
