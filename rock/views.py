from django.shortcuts import render
from rock.models import Performers


def default(request):
    return render(request, 'allGenres.html')


def performers_1(request):
    context = {'performers': Performers.objects.all()}

    return render(request, "description.html", context=context)


def performers_2(request, personality):

    return render(request, 'performers.html', context={'person': Performers.objects.get(id=personality)})
