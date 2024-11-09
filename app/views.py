from django.shortcuts import render

from models.question import get_by_id, get_by_tag
from models.answer import get_by_question_id
from models.question import mock_questions
from models.user import mock_user
from app.pagination import paginate

def index(request):
    questions = mock_questions
    page = paginate(request, questions)
    return render(request, 'index.html', {'questionCards': page.object_list, "page": page})


def ask(request):
    return render(request, 'ask.html')


def question(request, question_id):
    question = get_by_id(question_id)
    answers = get_by_question_id(question_id)
    page = paginate(request, answers)
    return render(request, 'question.html', {'question': question, 'answers': page.object_list, "page": page})


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')

def tagged(request, tag_name):
    questions = get_by_tag(tag_name)
    page = paginate(request, questions)
    return render(request, 'tagged.html', context={'tag_name': tag_name, 'questionCards': page.object_list, "page": page})

def settings(request):
    print(mock_user)
    return render(request, 'settings.html', context={'user': mock_user})

def hot(request):
    questions = mock_questions
    questions.reverse()
    page = paginate(request, questions)
    return render(request, 'hot.html', context={'questions': page.object_list, "page": page})