from django.conf.urls.static import static


class Answer:
    def __init__(self, iden, author, upvotes, text, is_correct, question):
        self._id = iden
        self._author = author
        self._upvotes = upvotes
        self._text = text
        self._is_correct = is_correct
        self._question = question

    def __repr__(self):
        return f"Answer(id={self.id}, author={self._author}, upvotes={self._upvotes}, is_correct={self._is_correct}, question={self._question})"

    def id(self):
        return self._id

    def author(self):
        return self._author

    def upvotes(self):
        return self._upvotes

    def text(self):
        return self._text

    def is_correct(self):
        return self._is_correct

    def question(self):
        return self._question

mock_answers = [
        Answer(
            iden=1,
            author='Anna',
            upvotes=4,
            text='Чтобы установить Python на Windows, загрузите установочный файл с официального сайта и следуйте инструкциям. Для macOS используйте команду `brew install python`, если Homebrew уже установлен.',
            is_correct=True,
            question=1
        ),
        Answer(
            iden=2,
            author='Ivan',
            upvotes=2,
            text='На Windows откройте установочный файл и выберите опцию "Add Python to PATH". На Mac можете скачать Python с сайта или использовать команду `pyenv`.',
            is_correct=False,
            question=1
        ),
        Answer(
            iden=3,
            author='Olga',
            upvotes=5,
            text='Объектно-ориентированное программирование включает понятия классов, объектов, наследования, инкапсуляции и полиморфизма. Основная идея — представление данных в виде объектов.',
            is_correct=True,
            question=2
        ),
        Answer(
            iden=4,
            author='Nikita',
            upvotes=1,
            text='OOP — это подход к программированию, где данные и методы для их обработки объединены в классы, что упрощает поддержку кода.',
            is_correct=False,
            question=2
        ),
        Answer(
            iden=5,
            author='Dmitry',
            upvotes=3,
            text='Git позволяет разработчикам отслеживать изменения в коде и совместно работать над проектами. Основные команды — `git init`, `git clone`, `git commit`, `git push`, `git pull`.',
            is_correct=True,
            question=3
        ),
        Answer(
            iden=6,
            author='Maria',
            upvotes=0,
            text='Git — это распределённая система контроля версий, позволяющая создавать и объединять ветки для удобной работы над проектом.',
            is_correct=False,
            question=3
        ),
        Answer(
            iden=7,
            author='Alexey',
            upvotes=4,
            text='API — это интерфейс, который позволяет взаимодействовать с другими приложениями. Например, чтобы получить данные с сервера, можно отправить HTTP-запрос к API.',
            is_correct=True,
            question=4
        ),
        Answer(
            iden=8,
            author='Elena',
            upvotes=2,
            text='API — это набор методов и протоколов, которые позволяют разным приложениям обмениваться данными. Он часто используется для интеграции различных сервисов.',
            is_correct=False,
            question=4
        ),
        Answer(
            iden=9,
            author='Sergey',
            upvotes=6,
            text='Начать лучше всего с выбора языка программирования, например, Python. Изучайте основы и постепенно переходите к более сложным темам, решая задачи.',
            is_correct=True,
            question=5
        ),
        Answer(
            iden=10,
            author='Nina',
            upvotes=1,
            text='Учиться программировать лучше всего с практики. Начните с небольших проектов и учитесь на реальных задачах, одновременно осваивая теорию.',
            is_correct=False,
            question=5
        )
    ]

def get_by_question_id(question_id):
    answer_list = []
    for answer in mock_answers:
        if answer.question() == question_id:
            answer_list.append(answer)
    return answer_list