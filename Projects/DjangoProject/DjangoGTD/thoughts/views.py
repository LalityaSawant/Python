from django.shortcuts import render
# from django.http import HttpResponse
from .models import Inpile

# testing
# thoughts = [
#     {
#      'task': 'Do something',
#      'task_type': 'SomeDayMayBe',
#      'eta': 'July, 1, 2020'
#     },
#     {
#      'task': 'Learn Python',
#      'task_type': 'ToDO',
#      'eta': 'July, 10, 2020'
#     }
# ]


def home(request):
    # return HttpResponse('<h1>GTD Home</h1>')

    context = {
        'thoughts': Inpile.objects.all()
    }

    return render(request, 'thoughts/home.html', context)


def about(request):
    return render(request, 'thoughts/about.html', {'title': 'About'})
