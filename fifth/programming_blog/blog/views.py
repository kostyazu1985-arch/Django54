from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.core.mail import send_mail
from django.contrib import messages
from .utils import DataMixin


# Create your views here.

class BlogHome(ListView):
    model = Blog
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context


class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = "blog/contact.html"
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Обратная связь")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        name = form.cleaned_data['name']
        user_email = form.cleaned_data['email']
        content = form.cleaned_data['content']

        from_email = "kostyazu2014@yandex.ru"

        to_email = ["kostyazu2014@yandex.ru", "kostyazu2014@yandex.ru"]

        subject = f"Сообщение от {name} с сайта"

        body = f"""
            Имя: {name}
            Email пользователя: {user_email}
            Сообщение: {content}
        """

        if self.send_contact_email(subject, body, from_email, to_email, name):
            messages.success(self.request, "Сообщение отправлено успешно!")
            return super().form_valid(form)
        else:
            messages.error(self.request, "Ошибка при отправке!")
            return self.form_invalid(form)

    def send_contact_email(self, subject, body, from_email, to_email, name):
        try:
            send_mail(subject=subject, message=body, from_email=from_email, recipient_list=[to_email], fail_silently=False)
            return True
        except Exception as e:
            print(f"Ошибка при отправке письма: {e}")
            return False


