from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    sub = Subjects.objects.all()
    context = {
        'subject': sub
    }
    return render(request, 'index.html', context)


def sub(request, name):
    vid = Topics.objects.all()
    context = {
        'a': vid,
        'name': name
    }
    return render(request, 'subject.html', context)

def topic(request, n):
    vid = Topics.objects.get(pk=n)
    context = {
        'a': vid
    }
    return render(request, 'topic.html', context)
