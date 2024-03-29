from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse, Http404, HttpResponseRedirect 
from qa.models import *
from qa.forms import AskForm, AnswerForm, LoginForm, SignupForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def get_page(request):
    try:
        page = int(request.GET.get('page'))
    except ValueError:
        page = 1
    except TypeError:
        page = 1
    questions = Question.objects.all().order_by('-id')
    paginator = Paginator(questions, 10)
    page = paginator.page(page)
    return render(request, 'list.html',
                              {'title': 'New',
                               'paginator': paginator,
                               'questions': page.object_list,                                                                   'page': page, 
                               }
                 )
def get_popular(request):
    try:
        page = int(request.GET.get('page'))
    except ValueError:
        page = 1
    except TypeError:
        page = 1
    questions = Question.objects.all().order_by('-rating')
    paginator = Paginator(questions, 10)
    page = paginator.page(page)
    return render(request, 'list.html',
                              {'title': 'Pop',
                               'paginator': paginator,
                               'questions': page.object_list,                                                                   'page': page, 
                               }
                 )
   
def get_question(request, num):
    try:
        q = Question.objects.get(id=num)
    except Question.DoesNotExist:
        raise Http404
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            form._user = request.user
            _ = form.save()
            url = q.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm(initial={'question': q.id})

    return render(request, 'question.html', {'question': q,
                                             'form': form,
                                            })

def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            form._user = request.user
            q = form.save()
            url = q.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'ask.html', {'form': form, })

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid(): 
            user = form.save()
            name = form.cleaned_data['username']
            password = form.raw_password
            user = authenticate(username=name, password=password)
            print(type(user))
            if user is not None:
                if user.is_active:
                    login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form,
                                               'user': request.user,
                                               })

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            print(username, password)
            user = authenticate(username=username, password=password)
            print(type(user))
            if user is not None:
                if user.is_active:
                    login(request, user)
        return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form,
                                          'user': request.user,
                                              })





