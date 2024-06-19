import re
from typing import List

import requests

from DataTransferObject.BibleBooks import BibleBooks
from DataTransferObject.VerseDTO import VerseDTO


def _get_book_index(books_name_chinese: str):
    index = BibleBooks.CHINESE.index(books_name_chinese)
    assert index >= 0
    return index + 1


def _remove_html_tags(text: str):
    return re.sub(r'<.*?>', '', text)


def _remove_parentheses(text: str):
    cleaned_text = re.sub(r'〔.*?〕', '', text)
    cleaned_text = re.sub(r'\(.*?\)', '', cleaned_text)
    return cleaned_text


class BibleQueryService:

    def __init__(self):

        self.get_text_endpoint = "https://bolls.life/get-text"
        self.get_verse_endpoint = "https://bolls.life/get-verse"
        self.translation_short_name = "CUNPS"

    def get_verses(self, verses: List[VerseDTO]):
        result = []
        for verse in verses:
            book_idx = _get_book_index(verse.book)
            query_string = f'{self.get_verse_endpoint}/{self.translation_short_name}/{book_idx}/{verse.chapter}/{verse.verse}'
            response = requests.get(query_string)
            assert response.status_code == 200
            verse_text = response.json()['text']
            cleaned_verse_text = _remove_html_tags(verse_text)
            cleaned_verse_text = _remove_parentheses(cleaned_verse_text)
            result.append(cleaned_verse_text)

        return result
