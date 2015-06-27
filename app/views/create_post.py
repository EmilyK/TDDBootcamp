from django.views.generic import FormView
from app.forms.create_post import CreatePostForm
from app.models import Post


class CreatePost(FormView):
    template_name = 'posts/create.html'
    form_class = CreatePostForm
    context_object_name = 'form'
    # post = Post.objects.get(pk=kwargs['pk'])
    success_url = ''

    def post(self, request, *args, **kwargs):
        form = self.get_form(form_class=CreatePost.form_class)
        if form.is_valid():
            post = Post.objects.create(**form.cleaned_data)
            CreatePost.success_url = '%d/' % post.id
        return super(CreatePost, self).post(request, args, kwargs)