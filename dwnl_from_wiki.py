"""
Модуль реализует взаимодействие с API
Wikipedia
"""
import wikipedia as wiki


def get_wiki_info(word: str):
    wiki.set_lang('ru')
    print(word)
    """
    :param word:искомое слово для поиска
    :return:
    результат поиска по ключевому слову
    """
    info = f'По запросу {word} ничего не найдено'
    try:
        info = wiki.summary(word)
    finally:
        return info
