from django import forms
from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    name = forms.CharField(label="Имя", max_length=100)
    email = forms.EmailField(label="Email")
    content = forms.CharField(label="Сообщение", widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    captcha = CaptchaField()