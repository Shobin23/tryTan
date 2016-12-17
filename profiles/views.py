from django.views import generic
from .models import Datamain,Subtask
from django.shortcuts import render

class IndexView(generic.ListView):
	template_name='profiles/index.html'


	def get_queryset(self):
		return Datamain.objects.all()

class DetailView(generic.DetailView):
	model = Datamain
	template_name= 'profiles/details.html'
	
	def get_queryset(self):
		return Datamain.objects.all()
	

'''def detail(request, task_details):
    # return HttpResponse("<h2>Details For Task:"+str(task_details)+ "</h2>")
    try:
        task = Datamain.objects.get(pk=task_details)
    except Datamain.DoesNotExist:
        raise Http404("Task does not exist")
    return render(request, 'profiles/details.html', {'task': task})'''

