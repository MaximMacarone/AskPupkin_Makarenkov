from django.shortcuts import render, get_object_or_404

from AskPupkin_Makarenkov.models.question import Question, get_by_id
from AskPupkin_Makarenkov.models.answer import Answer, get_by_question_id
from AskPupkin_Makarenkov.models.question import mock_questions


def base(request):
    return render(request, 'base.html')


def index(request):
    questions = mock_questions
    return render(request, 'index.html', {'questionCards': questions})


def ask(request):
    return render(request, 'ask.html')


def question(request, question_id):
    question = get_by_id(question_id)
    answers = get_by_question_id(question_id)
    return render(request, 'question.html', {'question': question, 'answers': answers})


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')
