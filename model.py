"""
Модуль выполняет загрузку модели
и предподготовку изображения
"""

from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.efficientnet import (preprocess_input,
                                                        decode_predictions)
import numpy as np


def load_model():
    """
    Выполняет конфигурацию модели
    :return: объект EfficientNetB0(
    """
    model = EfficientNetB0(weights='imagenet')
    return model


def preprocess_image(img):
    """
    Выполняет настройку препроцессора
    картинки
    :param img:
    :return: объект для
    подготовки картинки
    """
    img = img.resize((224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return x


def get_predictions(prd):
    """
    Получает предиктор
    :param prd: объект предиктор
    :return: предиктор
    """
    return decode_predictions(prd, top=1)[0]
