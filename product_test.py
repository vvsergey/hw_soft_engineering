from fastapi.testclient import TestClient
import api


client = TestClient(api.app)


def test_read_maim():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "Success"}


def test_predict_dog():
    files = {'file': open('images/dog.jpeg', 'rb')}
    response = client.post('/', files=files)
    assert response.json() == ["Labrador_retriever"]
    assert response.status_code == 200


def test_predict_cat():
    files = {'file': open('images/cat.jpeg', 'rb')}
    response = client.post('/', files=files)
    assert response.status_code == 200
    assert response.json() == ["Egyptian_cat"]
