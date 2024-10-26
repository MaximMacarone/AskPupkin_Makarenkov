from django.shortcuts import render

from AskPupkin_Makarenkov.models.question import Question


def base(request):
    return render(request, 'base.html')
def index(request):
    questions = Question.get_mock_questions()
    return render(request, 'index.html', {'questionCards': questions})

def ask(request):
    return render(request, 'ask.html')

def question(request, question_id):
    return render(request, 'question.html', {'question': Question.get_by_id(question_id)})

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')