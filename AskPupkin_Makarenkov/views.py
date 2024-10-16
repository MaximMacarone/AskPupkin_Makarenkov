from django.shortcuts import render

from AskPupkin_Makarenkov.models.question import Question


def base(request):
    return render(request, 'static/base.html')

def index(request):
    questions = Question.get_mock_questions()
    return render(request, 'static/index.html', {'questionCards': questions})

def ask(request):
    return render(request, 'static/ask.html')