"""
Модуль реализует приложение средствами Streamlit
"""
from PIL import Image
import io
import model as mdl
import streamlit as st
import dwnl_from_wiki as from_wiki



def load_image():
    """
    Создает форму для загрузки
    изображения средствами Streamlit
    :return: десериализованный объект изображения
    """
    uploaded_file = (st.file_uploader
                     (label='Выберите изображение для распознавания'))
    if uploaded_file is not None:
        # Получение загруженного изображения
        image_data = uploaded_file.getvalue()
        # Показ загруженного изображения на Web-странице средствами Streamlit
        st.image(image_data)
        # Возврат изображения в формате PIL
        return Image.open(io.BytesIO(image_data))
    else:
        return None


# Загружаем предварительно обученную модель
model = mdl.load_model()
# Выводим заголовок страницы
st.title('Классификация изображений')
# Выводим форму загрузки изображения и получаем изображение
img = load_image()
# Показывам кнопку для запуска распознавания изображения
result = st.button('Распознать изображение')
recognize = ''
# Если кнопка нажата, то запускаем распознавание изображения
if result:
    # Предварительная обработка изображения
    x = mdl.preprocess_image(img)
    # Распознавание изображения
    prd = model.predict(x)
    # Выводим заголовок результатов распознавания жирным шрифтом
    # используя форматирование Markdown
    st.write('**Результаты распознавания:**')
    recognize += mdl.get_predictions(prd)[0][1]
    st.write(recognize)
    st.write(from_wiki.get_wiki_info(recognize))
    # Выводим результаты распознавания
