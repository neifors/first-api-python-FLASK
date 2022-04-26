''' Films controller '''
from werkzeug.exceptions import BadRequest

films = [
    {'id': 1, 'name': 'Harry Potter', 'year': 1998},
    {'id': 2, 'name': 'Lord of Rings', 'year': 2000},
    {'id': 3, 'name': 'The notebook', 'year': 1992}
]

def index(req):
    return [film for film in films], 200

def show(req, uid):
    return find_by_uid(uid), 200

def create(req):
    new_film = req.get_json()
    new_film['id'] = sorted([film['id'] for film in films])[-1] + 1
    films.append(new_film)
    return new_film, 201

def update(req, uid):
    film = find_by_uid(uid)
    data = req.get_json()
    print(data)
    for key, val in data.items():
        film[key] = val
    return film, 200

def destroy(req, uid):
    film = find_by_uid(uid)
    films.remove(film)
    return film, 204

def find_by_uid(uid):
    try:
        return next(film for film in films if film['id'] == uid)
    except:
        raise BadRequest(f"We don't have that film with id {uid}!")
