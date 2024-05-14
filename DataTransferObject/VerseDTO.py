class VerseDTO:

    # List of the 66 Bible books in Chinese
    BIBLE_BOOKS_CHINESE = [
        "创世记", "出埃及记", "利未记", "民数记", "申命记", "约书亚记", "士师记", "路得记", "撒母耳记上",
        "撒母耳记下", "列王纪上", "列王纪下", "历代志上", "历代志下", "以斯拉记", "尼希米记", "以斯帖记",
        "约伯记", "诗篇", "箴言", "传道书", "雅歌", "以赛亚书", "耶利米书", "耶利米哀歌", "以西结书",
        "但以理书", "何西阿书", "约珥书", "阿摩司书", "俄巴底亚书", "约拿书", "弥迦书", "那鸿书", "哈巴谷书",
        "西番雅书", "哈该书", "撒迦利亚书", "玛拉基书", "马太福音", "马可福音", "路加福音", "约翰福音",
        "使徒行传", "罗马书", "哥林多前书", "哥林多后书", "加拉太书", "以弗所书", "腓立比书", "歌罗西书",
        "帖撒罗尼迦前书", "帖撒罗尼迦后书", "提摩太前书", "提摩太后书", "提多书", "腓利门书", "希伯来书",
        "雅各书", "彼得前书", "彼得后书", "约翰一书", "约翰二书", "约翰三书", "犹大书", "启示录"
    ]

    def __init__(self, book: str, chapter: int, verse: int):
        if book not in VerseDTO.BIBLE_BOOKS_CHINESE:
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
