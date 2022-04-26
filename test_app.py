import json

class TestAPICase():
    def test_welcome(self, api):
        res = api.get('/')
        assert res.status == '200 OK'
        assert res.json['message'] == 'Hello from Flask!'

    def test_get_films(self, api):
        res = api.get('/api/films')
        assert res.status == '200 OK'
        assert len(res.json) == 2

    def test_get_film(self, api):
        res = api.get('/api/films/2')
        assert res.status == '200 OK'
        assert res.json['name'] == 'Test Film 2'

    def test_get_film_error(self, api):
        res = api.get('/api/films/4')
        assert res.status == '400 BAD REQUEST'
        assert "film with id 4" in res.json['message']

    def test_post_films(self, api):
        mock_data = json.dumps({'name': 'Saw'})
        mock_headers = {'Content-Type': 'application/json'}
        res = api.post('/api/films', data=mock_data, headers=mock_headers)
        assert res.json['id'] == 3

    def test_patch_Film(self, api):
        mock_data = json.dumps({'name': 'Rocky'})
        mock_headers = {'Content-Type': 'application/json'}
        res = api.patch('/api/films/2', data=mock_data, headers=mock_headers)
        assert res.json['id'] == 2
        assert res.json['name'] == 'Rocky'

    def test_delete_film(self, api):
        res = api.delete('/api/films/1')
        assert res.status == '204 NO CONTENT'

    def test_not_found(self, api):
        res = api.get('/bob')
        assert res.status == '404 NOT FOUND'
        assert 'Oops!' in res.json['message']
