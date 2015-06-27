
from django.test import TestCase
from app.models import Post


class PostTest(TestCase):
    def test_should_return_title_as_a_string_representation(self):
        post= Post(title= 'Yoyo!', body= 'Whats up')
        self.assertEquals(post.title, post.__str__())

