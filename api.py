"""
Модуль реализует API на FastAPI
для приложения по распознаванию изображения
"""
from PIL import Image
from fastapi import FastAPI, UploadFile, File
import model as mdl
import dwnl_from_wiki as from_wiki


app = FastAPI()

model = mdl.load_model()


@app.get('/')
def root():
    """
    Метод возвращает сообщение
    об успешном подключении к серверу
    :return: dict
    """
    return {"message": "Success"}


@app.post('/')
async def predict_process(file: UploadFile = File(...)):
    """
    Классифицирует изображение с
    использованием модели
    :param file: принимать картинку
    :return: результат распознавания
    загруженной картинки
    """
    img = Image.open(file.file)
    x = mdl.preprocess_image(img)
    prd = model.predict(x)
    cls = mdl.get_predictions(prd)
    return {cls[0][1]}


@app.get('/')
async def get_wiki_info(word: str):
    """
    метод извлекает краткую тезисную
    информацию из wiki
    :param word: слово для поиска
    :return: результат поиска вики
    """
    return from_wiki.get_wiki_info(word)

