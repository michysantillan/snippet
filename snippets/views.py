from django.db.models.aggregates import Count
from snippets.models import Snippet
from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView, DetailView, CreateView, View
from .forms import SnippetForm, SnippetUpdateForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


def login(request):
    return render(request, 'login.html', {})


def logout(request):
    return render(request, 'login.html', {})


def index(request):
    return render(request, 'index.html', {})


def language(request):
    return render(request, 'index.html', {})


def user_snippets(request):
    return render(request, 'snippets/user_snippets.html', {})


def snippet(request):
    return render(request, 'snippets/snippet.html', {})


def snippet_add(request):
    return render(request, 'snippets/snippet_add.html', {})


def snippet_edit(request):
    return render(request, 'snippets/snippet_add.html', {})


def snippet_delete(request):
    return render(request, 'snippets/user_snippets.html', {})

class SnippetList(ListView):
    model = Snippet
    #paginate_by = 20
    template_name = 'index.html'
 
    def get_queryset(self):
        return self.model.objects.all().order_by('id').filter(public=True)

class SnippetCreate(LoginRequiredMixin,CreateView):
    model = Snippet
    form_class = SnippetForm
    login_url = 'login'
    
    template_name = 'snippets/snippet_add.html'
    success_url = reverse_lazy('index')

class SnippetDetail(DetailView):
    model = Snippet    
    template_name = 'snippets/snippet.html'
    

class SnippetUpdate(LoginRequiredMixin,UpdateView):
    model = Snippet
    form_class = SnippetUpdateForm
    template_name = 'snippets/snippet_edit.html'    
    success_url = reverse_lazy('index')

 

class SnippetDelete(LoginRequiredMixin,DeleteView):
    model = Snippet
    template_name = 'snippets/snippet_delete.html'   
    success_url = reverse_lazy('index')


class UserSnippetList(LoginRequiredMixin,ListView):
   model = Snippet
   template_name = 'snippets/user_snippets.html'

   def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

class SnippetLangList(ListView):
    model = Snippet
    template_name = 'snippets/snippet_language.html'
 
 
    def get_queryset(self):
        return self.model.objects.all().filter(public=True).order_by('language').reverse()

