"""
Модуль реализует взаимодействие с API
Wikipedia
"""
import wikipedia as wiki


def get_wiki_info(query: str):
    """
    :param query:искомое слово для поиска
    :return:
    результат поиска по ключевому слову
    """
    wiki.set_lang('ru')
    query_result = f'По запросу {query} ничего не найдено'
    try:
        query_result = wiki.summary(query)
    finally:
        return query_result

