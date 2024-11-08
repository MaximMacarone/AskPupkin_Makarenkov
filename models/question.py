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


mock_questions = [
    Question(
        id=1,
        author='Maxim',  # Should be an ID
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
    ),
    Question(
        id=6,
        author='Maxim',
        title='Как установить Django?',
        text='Можете рассказать, как установить Django и настроить проект?',
        tags=['django', 'установка', 'python'],
        upvotes=5,
    ),
    Question(
        id=7,
        author='Maxim',
        title='Что такое REST API?',
        text='Объясните, что такое REST API и для чего он используется.',
        tags=['api', 'rest', 'разработка'],
        upvotes=8,
    ),
    Question(
        id=8,
        author='Maxim',
        title='Как работает SQL?',
        text='Поделитесь основами работы с SQL и базами данных.',
        tags=['sql', 'базы данных', 'запросы'],
        upvotes=3,
    ),
    Question(
        id=9,
        author='Maxim',
        title='Что такое GitHub?',
        text='Расскажите о возможностях GitHub и как начать с ним работать.',
        tags=['github', 'git', 'контроль версий'],
        upvotes=6,
    ),
    Question(
        id=10,
        author='Maxim',
        title='Как написать Hello World на JavaScript?',
        text='Объясните, как написать самое простое приложение на JavaScript.',
        tags=['javascript', 'программирование', 'начинающие'],
        upvotes=2,
    ),
    Question(
        id=11,
        author='Maxim',
        title='Как работают веб-серверы?',
        text='Поделитесь основами работы веб-серверов и HTTP-запросов.',
        tags=['веб-сервер', 'http', 'разработка'],
        upvotes=9,
    ),
    Question(
        id=12,
        author='Maxim',
        title='Что такое алгоритмы?',
        text='Объясните, что такое алгоритмы и зачем они нужны в программировании.',
        tags=['алгоритмы', 'программирование', 'базовые'],
        upvotes=10,
    ),
    Question(
        id=13,
        author='Maxim',
        title='Как настроить виртуальное окружение?',
        text='Как создать и настроить виртуальное окружение в Python?',
        tags=['python', 'виртуальное окружение', 'настройка'],
        upvotes=4,
    ),
    Question(
        id=14,
        author='Maxim',
        title='Что такое HTML и CSS?',
        text='Расскажите о роли HTML и CSS в веб-разработке.',
        tags=['html', 'css', 'веб-разработка'],
        upvotes=7,
    ),
    Question(
        id=15,
        author='Maxim',
        title='Какие существуют типы данных?',
        text='Объясните основные типы данных в программировании.',
        tags=['типы данных', 'базовые', 'программирование'],
        upvotes=5,
    ),
    Question(
        id=16,
        author='Maxim',
        title='Что такое фреймворк?',
        text='Поясните, что такое фреймворк и зачем он нужен в разработке.',
        tags=['фреймворк', 'разработка', 'базовые'],
        upvotes=6,
    ),
    Question(
        id=17,
        author='Maxim',
        title='Как оптимизировать SQL-запросы?',
        text='Поделитесь основными методами оптимизации SQL-запросов.',
        tags=['sql', 'оптимизация', 'базы данных'],
        upvotes=12,
    ),
    Question(
        id=18,
        author='Maxim',
        title='Что такое модульное тестирование?',
        text='Расскажите об основах модульного тестирования и его преимуществах.',
        tags=['тестирование', 'модульное', 'разработка'],
        upvotes=9,
    ),
    Question(
        id=19,
        author='Maxim',
        title='Как работает память в Python?',
        text='Объясните, как Python управляет памятью и что такое сборщик мусора.',
        tags=['python', 'память', 'оптимизация'],
        upvotes=11,
    ),
    Question(
        id=20,
        author='Maxim',
        title='Что такое JSON?',
        text='Объясните, что такое JSON и где его используют.',
        tags=['json', 'форматы данных', 'веб'],
        upvotes=3,
    ),
    Question(
        id=21,
        author='Maxim',
        title='Как создать REST API на Django?',
        text='Поделитесь основами создания REST API на Django.',
        tags=['django', 'api', 'разработка'],
        upvotes=8,
    ),
    Question(
        id=22,
        author='Maxim',
        title='Что такое Docker и как его использовать?',
        text='Расскажите о Docker и как начать его использовать.',
        tags=['docker', 'контейнеризация', 'разработка'],
        upvotes=10,
    ),
    Question(
        id=23,
        author='Maxim',
        title='Как работать с асинхронностью в Python?',
        text='Поделитесь основами асинхронного программирования в Python.',
        tags=['python', 'асинхронность', 'программирование'],
        upvotes=7,
    ),
    Question(
        id=24,
        author='Maxim',
        title='Что такое ORM?',
        text='Объясните, что такое ORM и зачем она нужна в работе с базами данных.',
        tags=['orm', 'базы данных', 'django'],
        upvotes=5,
    ),
    Question(
        id=25,
        author='Maxim',
        title='Как работать с API на Python?',
        text='Поделитесь основами взаимодействия с API на Python.',
        tags=['api', 'python', 'разработка'],
        upvotes=6,
    ),
    Question(
        id=26,
        author='Maxim',
        title='Как изучить JavaScript?',
        text='С чего начать изучение JavaScript для веб-разработки?',
        tags=['javascript', 'обучение', 'веб-разработка'],
        upvotes=7,
    ),
    Question(
        id=27,
        author='Maxim',
        title='Что такое классы в Python?',
        text='Объясните, что такое классы в Python и как с ними работать.',
        tags=['python', 'классы', 'oop'],
        upvotes=4,
    ),
    Question(
        id=28,
        author='Maxim',
        title='Как организовать проект на Django?',
        text='Поделитесь советами по структурированию проекта на Django.',
        tags=['django', 'организация проекта', 'структура'],
        upvotes=6,
    ),
    Question(
        id=29,
        author='Maxim',
        title='Что такое хэширование?',
        text='Расскажите о хэшировании данных и его применении.',
        tags=['хэширование', 'безопасность', 'данные'],
        upvotes=5,
    ),
    Question(
        id=30,
        author='Maxim',
        title='Как настроить SSL-сертификат?',
        text='Объясните процесс настройки SSL-сертификата на сервере.',
        tags=['ssl', 'сертификаты', 'безопасность'],
        upvotes=9,
    ),
    Question(
        id=31,
        author='Maxim',
        title='Как защитить веб-приложение?',
        text='Какие меры безопасности можно применить для веб-приложений?',
        tags=['безопасность', 'веб-приложения', 'разработка'],
        upvotes=10,
    ),
    Question(
        id=32,
        author='Maxim',
        title='Что такое асинхронные функции?',
        text='Объясните концепцию асинхронных функций и их использование.',
        tags=['асинхронность', 'функции', 'программирование'],
        upvotes=8,
    ),
    Question(
        id=33,
        author='Maxim',
        title='Как работает виртуальная память?',
        text='Расскажите об основах работы виртуальной памяти в компьютерах.',
        tags=['виртуальная память', 'компьютеры', 'оптимизация'],
        upvotes=4,
    ),
    Question(
        id=34,
        author='Maxim',
        title='Что такое SOLID?',
        text='Объясните принципы SOLID в объектно-ориентированном программировании.',
        tags=['solid', 'oop', 'принципы'],
        upvotes=12,
    ),
    Question(
        id=35,
        author='Maxim',
        title='Как работает шифрование данных?',
        text='Объясните основные принципы шифрования данных и их применение.',
        tags=['шифрование', 'безопасность', 'данные'],
        upvotes=11,
    )
]