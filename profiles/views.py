from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Datamain, Subtask
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy



class IndexView(generic.ListView):
    template_name = 'profiles/index.html'

    def get_queryset(self):
        return Datamain.objects.all()

class SubIndexView(generic.ListView):
    template_name = 'profiles/details.html'

    def get_queryset(self):
        return Subtask.objects.all()


class DetailView(generic.DetailView):
    model = Datamain
    template_name = 'profiles/details.html'

class TaskCreate(CreateView):
    model=Datamain
    fields=['main_task','date_time','efforts','status']

class TaskUpdate(UpdateView):
    model=Datamain
    fields=['main_task','date_time','efforts','status']

class TaskDelete(DeleteView):
    model=Datamain
    success_url = reverse_lazy('profiles:index')
    fields=['main_task','date_time','efforts','status']

class SubTaskCreate(CreateView):
    model=Subtask
    fields=['sub_task','comments','status']
    success_url = reverse_lazy('profiles:index')


