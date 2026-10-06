from django import forms
# from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    name = forms.CharField(label="Имя", max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-input'}))
    content = forms.CharField(label="Сообщение", widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    # captcha = CaptchaField()