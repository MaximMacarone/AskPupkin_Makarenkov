import uuid


class User:
    def __init__(self, nickname, avatar, login, email):
        self._id = str(uuid.uuid4())
        self._nickname = nickname
        self._avatar = avatar
        self._login = login
        self._email = email

    def nickname(self):
        return self._nickname

    def avatar(self):
        return self._avatar

    def login(self):
        return self._login

    def email(self):
        return self._email


    @classmethod
    def get_avatar_by_id(cls, user_id):
        return "image.jpg"


mock_user = User("Dr.Pepper", "image.jpg", "dr_pepper", "drpepper@gmail.com" )