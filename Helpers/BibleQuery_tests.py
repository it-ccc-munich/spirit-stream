from DataTransferObject.VerseDTO import VerseDTO
from Helpers.BibleQuery import BibleQueryService

if __name__ == '__main__':
    verse1 = VerseDTO("创世记", 1, 1)
    verse2 = VerseDTO("雅歌", 8, 1)
    verse3 = VerseDTO("雅歌", 8, 4)
    bibleQueryService = BibleQueryService()
    result = bibleQueryService.get_verses([verse1, verse2, verse3])
    print(result)
