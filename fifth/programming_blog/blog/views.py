from django.shortcuts import render
from django.views.generic import ListView, FormView

from .models import *
from .forms import *


# Create your views here.
menu = [
    {'title': 'Добавить статью', 'url_name': 'index'},
    {'title': 'Выйти', 'url_name': 'index'}
]


class BlogHome(ListView):
    model = Blog
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['menu'] = menu
        return context


# class ContactFormView():
#     form_class = ContactForm
#     template_name = "blog/contact.html"
#     success_url =


