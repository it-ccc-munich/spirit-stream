from typing import Union, List


class ContactDTO:

    def __init__(self, name: str, email: Union[str, None], alias: List[str] = []):
        # 名字
        self.name = name
        # Email联系方式
        self.email = email
        # 其他称呼
        self.alias = alias
