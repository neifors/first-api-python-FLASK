from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers import films
from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({'message': 'Hello from Flask!'}), 200

@app.route('/api/films', methods=['GET', 'POST'])
def cats_handler():
    fns = {
        'GET': films.index,
        'POST': films.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code

@app.route('/api/films/<int:film_id>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
def cat_handler(film_id):
    fns = {
        'GET': films.show,
        'PATCH': films.update,
        'PUT': films.update,
        'DELETE': films.destroy
    }
    resp, code = fns[request.method](request, film_id)
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
