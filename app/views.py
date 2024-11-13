from django.shortcuts import render, get_object_or_404

from app import models
from models.user import mock_user
from app.pagination import paginate

def index(request):
    questions = models.Question.objects.newest().all()
    page = paginate(request, questions)
    return render(request, 'index.html', {'questionCards': page.object_list, "page": page})

def page_not_found(request, exception):
    return render(request, '404page.html', status=404)

def ask(request):
    return render(request, 'ask.html')

def question(request, question_id):
    this_question = get_object_or_404(models.Question, pk=question_id)
    answers = this_question.answers.all()
    page = paginate(request, answers)
    return render(request, 'question.html', {'question': this_question, 'answers': page.object_list, "page": page})


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')

def tagged(request, tag_name):
    this_tag = get_object_or_404(models.Tag, name=tag_name)
    questions = models.Question.objects.tagged(this_tag.name).all()
    page = paginate(request, questions)
    return render(request, 'tagged.html', context={'tag_name': tag_name, 'questionCards': page.object_list, "page": page})

def settings(request):
    return render(request, 'settings.html', context={'user': mock_user})

def hot(request):
    questions = models.Question.objects.best().all()
    page = paginate(request, questions)
    return render(request, 'hot.html', context={'questions': page.object_list, "page": page})