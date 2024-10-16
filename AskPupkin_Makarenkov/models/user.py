
class User:
    def __init__(self, name, avatar):
        self.name = name
        self.avatar = avatar

    @classmethod
    def get_avatar_by_id(cls, user_id):
        return "image.jpg"