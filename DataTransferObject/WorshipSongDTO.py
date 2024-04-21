from typing import List


# TODO: Probably needs some adjustments when we move to PPT generation
class WorshipSongDTO:

    def __init__(self, name: str, subtitle: str, lyrics_paragraph: List[str]):
        # 歌曲名
        self.name = name
        # 小标题
        self.subtitle = subtitle
        # 歌词段落
        self.lyrics_paragraph = lyrics_paragraph
