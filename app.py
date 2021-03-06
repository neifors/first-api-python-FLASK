from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from controllers import films, more_films
from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
   return render_template("./index.html")

@app.route('/index.css')
def style():
   return render_template("./index.css")

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

@app.route('/outside/api/films')
def get_more_films():
    resp, code = more_films.index(request)
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
