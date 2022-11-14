from flask import Flask
import pytest

def create_app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    return app

@pytest.fixture()
def app():
    app = create_app()
    yield app

@pytest.fixture
def client(app):
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

def test_request_index(client):
    response = client.get("/")
    assert response.status == '200 OK'
