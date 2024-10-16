from django.http import HttpResponse, request
from django.shortcuts import render

from AskPupkin_Makarenkov.question import Question


def base(request):
    return render(request, 'static/base.html')

def index(request):
    questions = Question.get_mock_questions()
    return render(request, 'static/index.html', {'questionCards': questions})