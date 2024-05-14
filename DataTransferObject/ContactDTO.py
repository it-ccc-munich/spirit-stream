from typing import Union


class ContactDTO:

    def __init__(self, name: str, email: Union[str, None]):
        # 名字
        self.name = name
        # Email联系方式
        self.email = email
