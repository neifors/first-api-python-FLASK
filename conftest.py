import pytest
import app
from controllers import cats

@pytest.fixture
def api(monkeypatch):
    test_cats = [
        {'id': 1, 'name': 'Test Cat 1', 'age': 7},
        {'id': 2, 'name': 'Test Cat 2', 'age': 4}
    ]
    monkeypatch.setattr(cats, "cats", test_cats)
    api = app.app.test_client()
    return api