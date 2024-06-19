from DataTransferObject.BibleBooks import BibleBooks


class VerseDTO:

    def __init__(self, book: str, chapter: int, verse: int):
        if book not in BibleBooks.CHINESE:
            raise ValueError("Invalid book name. Please provide a valid Chinese name for one of the 66 Bible books.")
        # 书
        self.book = book
        # 章
        self.chapter = chapter
        # 节
        self.verse = verse


def format_scripture_abbreviation(
    start: VerseDTO,
    end: VerseDTO
):
    if start.book != end.book:
        return f"{start.book} {start.chapter}:{start.verse} - {end.book} {end.chapter}:{end.verse}"
    elif start.chapter != end.chapter:
        return f"{start.book} {start.chapter}:{start.verse} - {end.chapter}:{end.verse}"
    else:
        return f"{start.book} {start.chapter}:{start.verse}-{end.verse}"
