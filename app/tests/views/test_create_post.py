from django.test import TestCase, Client
from app.forms.create_post import CreatePostForm
from app.models import Post

class TestCreatePost(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_should_render_create_page(self):
        response = self.client.get('/posts/new/')
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response=response, template_name='posts/create.html')

    def test_get_should_return_create_form(self):
        response = self.client.get('/posts/new/')
        self.assertEqual(200, response.status_code)
        self.assertIn('form', response.context)
        self.assertIsInstance(response.context['form'], CreatePostForm)

    def test_post_should_save_valid_form(self):
        fields = {'title': "my blog",'body': "this is the body"}

        self.client.post('/posts/', data=fields)
        post = Post.objects.get(title=fields['title'])

        self.assertIsNotNone(post)
        self.assertEquals(fields['title'],  post.title)
        self.assertEquals(fields['body'],  post.body)

    def test_post_should_not_save_invalid_form(self):
        fields = {'title': '', 'body': ''}
        response = self.client.post('/posts/', data=fields)
        self.assertTemplateUsed(response=response, template_name='posts/create.html')
        self.assertIsNotNone(response.context['form'].errors)
        self.assertEquals(0, Post.objects.count())

    def test_valid_form_redirects_to_success_url(self):
        #Given that I have filled correct data
        fields = {'title': 'Hey', 'body': 'there'}
        #when I submit
        response = self.client.post('/posts/', data=fields)
        #Then I should be redirected to success url
        post = Post.objects.get(title = fields['title'])
        self.assertRedirects(response, '/posts/%d/' % post.id)

