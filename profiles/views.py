from django.shortcuts import render
from .models import Datamain
from django.http import HttpResponse
from django.http import Http404


def index(request):
    all_task = Datamain.objects.all()
    return render(request, 'profiles/index.html', {'all_task': all_task})

    '''for album in all_task:
		url='/home/' + str(album.id)
		html += '<a href="' + url + '">' + album.main_task+'</a><br>'''


def detail(request, task_details):
    # return HttpResponse("<h2>Details For Task:"+str(task_details)+ "</h2>")
    try:
        task = Datamain.objects.get(pk=task_details)
    except Datamain.DoesNotExist:
        raise Http404("Task does not exist")
    return render(request, 'profiles/details.html', {'task': task})
