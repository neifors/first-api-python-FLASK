import pytest
import app
from controllers import films

@pytest.fixture
def api(monkeypatch):
    test_films = [
        {'id': 1, 'name': 'Test Film 1', 'year': 7},
        {'id': 2, 'name': 'Test Film 2', 'year': 4}
    ]
    monkeypatch.setattr(films, "films", test_films)
    api = app.app.test_client()
    return api
