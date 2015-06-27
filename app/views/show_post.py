from django.views.generic import DetailView
from app.models import Post


class ShowPost(DetailView):
    model = Post
    template_name = 'posts/details.html'

