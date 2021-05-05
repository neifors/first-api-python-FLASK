''' Cats controller '''
from werkzeug.exceptions import BadRequest

cats = [
    {'id': 1, 'name': 'Zelda', 'age': 3},
    {'id': 2, 'name': 'Tigerlily', 'age': 9},
    {'id': 3, 'name': 'Salem', 'age': 500}
]

def index(req):
    return [c for c in cats], 200

def show(req, uid):
    return find_by_uid(uid), 200

def create(req):
    new_cat = req.get_json()
    new_cat['id'] = sorted([c['id'] for c in cats])[-1] + 1
    cats.append(new_cat)
    return new_cat, 201

def update(req, uid):
    cat = find_by_uid(uid)
    data = req.get_json()
    print(data)
    for key, val in data.items():
        cat[key] = val
    return cat, 200

def destroy(req, uid):
    cat = find_by_uid(uid)
    cats.remove(cat)
    return cat, 204

def find_by_uid(uid):
    try:
        return next(cat for cat in cats if cat['id'] == uid)
    except:
        raise BadRequest(f"We don't have that cat with id {uid}!")