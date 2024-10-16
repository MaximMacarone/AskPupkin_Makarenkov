class Question:
    def __init__(self, title, text, tags, id, author):
        self._id = id
        self._title = title
        self._author = author # Should be author's ID, not name
        self._text = text
        self._tags = tags
        self._upvotes = 0

    mock_questions = [
        {
            'id' : 1,
            'author' : 'Maxim',
            'title': 'Как установить Python?',
            'text': 'Можете рассказать, как установить Python на Windows и Mac?',
            'tags': ['python', 'установка', 'windows', 'mac'],
            'upvotes': 9,
        },
        {
            'id': 2,
            'author': 'Maxim',
            'title': 'Что такое OOP?',
            'text': 'Объясните основные концепции объектно-ориентированного программирования.',
            'tags': ['oоп', 'концепции', 'программирование'],
            'upvotes': 3,
        },
        {
            'id': 3,
            'author': 'Maxim',
            'title': 'Как работает Git?',
            'text': 'Поделитесь основами работы с системой контроля версий Git.',
            'tags': ['git', 'версии', 'контроль'],
            'upvotes': 0,
        },
        {
            'id': 4,
            'author': 'Maxim',
            'title': 'Что такое API?',
            'text': 'Как объяснить, что такое API и как с ним работать?',
            'tags': ['api', 'интеграция', 'разработка'],
            'upvotes': 5,
        },
        {
            'id': 5,
            'author': 'Maxim',
            'title': 'Как научиться программировать?',
            'text': 'С чего начать обучение программированию для начинающих?',
            'tags': ['программирование', 'обучение', 'начинающие'],
            'upvotes': 2,
        }
    ]

    @classmethod
    def get_mock_questions(cls):
        return cls.mock_questions

    @classmethod
    def get_by_id(cls, id):
        for question in cls.mock_questions:
            if question['id'] == id:
                return question
