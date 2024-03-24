"""
Модуль реализует тесты для API
"""
from fastapi.testclient import TestClient
import api


client = TestClient(api.app)


def test_read_maim():
    """
    Тест проверяет доступность
    приложения при обращении к корню сервера
    :return: none
    """
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "Success"}


def test_predict_dog():
    """
    Проверяет результат загрузки картинки
    на сервер и распознавания изображенной
    собаки породы Лабрадор
    :return: none
    """
    files = {'file': open('images/dog.jpeg', 'rb')}
    response = client.post('/', files=files)
    assert response.json() == ["Labrador_retriever"]
    assert response.status_code == 200


def test_predict_cat():
    """
    Проверяет результат загрузки картинки
    на сервер и распознавания изображенной
    кошки египетской породы
    :return: none
    """
    files = {'file': open('images/cat.jpeg', 'rb')}
    response = client.post('/', files=files)
    assert response.status_code == 200
    assert response.json() == ["Egyptian_cat"]
