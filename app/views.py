from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
from django.urls import reverse

from app import models
from app.forms import LoginForm, ProfileForm, UserForm, EditProfileForm, EditUserForm, AskQuestionForm, AddAnswerForm
from app.pagination import paginate

def index(request):
    questions = models.Question.objects.newest().all()
    page = paginate(request, questions)
    return render(request, 'index.html', {'questionCards': page.object_list, "page": page})

def page_not_found(request, exception):
    return render(request, '404page.html', status=404)

@login_required(login_url='login')
def ask(request):
    if request.method == 'POST':
        form = AskQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            tag_names = form.cleaned_data['tags']
            question.tags.set(tag_names)
            return redirect('question', question.id)
    else:
        form = AskQuestionForm()

    return render(request, 'ask.html', {'form': form})


def question(request, question_id):
    this_question = get_object_or_404(models.Question, pk=question_id)
    answers = this_question.answers.all()
    page = paginate(request, answers)
    paginator = page.paginator
    if request.method == 'POST':
        form = AddAnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.question = this_question
            answer.save()

            last_page_number = paginator.num_pages
            return redirect(f"{reverse('question', args=[question_id])}?page={last_page_number}#answer-{answer.id}")
    else:
        form = AddAnswerForm()
    return render(request, 'question.html', {'question': this_question, 'answers': page.object_list, "page": page, "form": form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST, request.FILES)
        if form.is_valid():
            user = auth.authenticate(request, **form.cleaned_data)
            if user:
                auth.login(request, user)
                return redirect(reverse('index'))
            else:
                return render(request, 'login.html', {'form': form, 'NotFound': True})
    else:
        return render(request, 'login.html', {'form': LoginForm(), 'NotFound': False})


def signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])

            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            auth.login(request, user)
            return redirect(reverse('index'))
        else:
            return render(request, 'signup.html', {'profile_form': profile_form, 'user_form': user_form})
    return render(request, 'signup.html', {'profile_form': ProfileForm(), 'user_form': UserForm()})


def tagged(request, tag_name):
    this_tag = get_object_or_404(models.Tag, name=tag_name)
    questions = models.Question.objects.tagged(this_tag.name).all()
    page = paginate(request, questions)
    return render(request, 'tagged.html', context={'tag_name': tag_name, 'questionCards': page.object_list, "page": page})

@login_required(login_url='login')
def settings(request):
    profile = get_object_or_404(models.Profile, user=request.user)

    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=request.user)
        profile_form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('settings')
    else:
        profile_form = EditProfileForm(instance=profile)
        user_form = EditUserForm(instance=request.user)

    return render(request, 'settings.html', context={'user': request.user.profile, 'user_form': user_form, 'profile_form': profile_form})


def hot(request):
    questions = models.Question.objects.best().all()
    page = paginate(request, questions)
    return render(request, 'hot.html', context={'questions': page.object_list, "page": page})

def logout(request):
    auth.logout(request)

    previous_page = request.META.get('HTTP_REFERER', reverse('index'))
    return redirect(previous_page)

