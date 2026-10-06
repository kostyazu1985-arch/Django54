from .models import Category
from django.db.models import Count

menu = [
    {'title': 'Добавить статью', 'url_name': 'index'},
    {'title': 'Обратная связь', 'url_name': 'contact'}
]

class DataMixin:
    paginate_page = 3

    def get_user_context(self, **kwargs):
        context = kwargs

        cats = Category.objects.annotate(blog_count=Count('blog'))

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu = [item for item in user_menu if item ['url_name'] != 'add_page']

        context['menu'] = user_menu
        context['cats'] = cats

        if 'cat_selected' not in context:
            context['cat_selected'] = 0

        return context