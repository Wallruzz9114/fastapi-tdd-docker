from app import server
from fastapi import FastAPI


def test_ping(test_app: FastAPI):
    response = test_app.get('/ping')
    assert response.status_code == 200
    assert response.json() == {"environment": "dev",
                               "ping": "pong!", "testing": True}
