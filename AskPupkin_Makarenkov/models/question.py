class Question:
    def __init__(self, title, text, tags, id, author, upvotes):
        self._id = id
        self._title = title
        self._author = author  # Должен быть ID автора, а не имя
        self._text = text
        self._tags = tags
        self._upvotes = upvotes

    def __repr__(self):
        return f"Question(id={self._id}, title={self._title}, author={self._author}, upvotes={self._upvotes})"

    def id(self):
        return self._id

    def title(self):
        return self._title

    def author(self):
        return self._author

    def text(self):
        return self._text

    def tags(self):
        return self._tags

    def upvotes(self):
        return self._upvotes

mock_questions = [
    Question(
        id=1,
        author='Maxim',  # Предполагается, что это ID автора, его можно заменить на числовое значение
        title='Как установить Python?',
        text='Можете рассказать, как установить Python на Windows и Mac?',
        tags=['python', 'установка', 'windows', 'mac'],
        upvotes=2,
    ),
    Question(
        id=2,
        author='Maxim',
        title='Что такое OOP?',
        text='Объясните основные концепции объектно-ориентированного программирования.',
        tags=['oop', 'концепции', 'программирование'],
        upvotes=4,
    ),
    Question(
        id=3,
        author='Maxim',
        title='Как работает Git?',
        text='Поделитесь основами работы с системой контроля версий Git.',
        tags=['git', 'версии', 'контроль'],
        upvotes=1,
    ),
    Question(
        id=4,
        author='Maxim',
        title='Что такое API?',
        text='Как объяснить, что такое API и как с ним работать?',
        tags=['api', 'интеграция', 'разработка'],
        upvotes=7,
    ),
    Question(
        id=5,
        author='Maxim',
        title='Как научиться программировать?',
        text='С чего начать обучение программированию для начинающих?',
        tags=['программирование', 'обучение', 'начинающие'],
        upvotes=11,
    )
]

def get_by_id(question_id):
    for question in mock_questions:
        if question.id() == question_id:
            return question

def get_by_tag(question_tag):
    result = []
    for question in mock_questions:
        for tag in question.tags():
            print(tag)
            if tag == question_tag:
                result.append(question)
                break
    return result