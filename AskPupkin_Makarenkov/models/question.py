class Question:
    def __init__(self, title, text, tags):
        self._title = title
        self._text = text
        self._tags = tags

    mock_questions = [
        {
            'title': 'Как установить Python?',
            'text': 'Можете рассказать, как установить Python на Windows и Mac?',
            'tags': ['python', 'установка', 'windows', 'mac']
        },
        {
            'title': 'Что такое OOP?',
            'text': 'Объясните основные концепции объектно-ориентированного программирования.',
            'tags': ['oоп', 'концепции', 'программирование']
        },
        {
            'title': 'Как работает Git?',
            'text': 'Поделитесь основами работы с системой контроля версий Git.',
            'tags': ['git', 'версии', 'контроль']
        },
        {
            'title': 'Что такое API?',
            'text': 'Как объяснить, что такое API и как с ним работать?',
            'tags': ['api', 'интеграция', 'разработка']
        },
        {
            'title': 'Как научиться программировать?',
            'text': 'С чего начать обучение программированию для начинающих?',
            'tags': ['программирование', 'обучение', 'начинающие']
        }
    ]

    @classmethod
    def get_mock_questions(cls):
        return cls.mock_questions