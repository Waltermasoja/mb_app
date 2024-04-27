from django.test import TestCase
from .models import Post
from django.urls import reverse

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text= "Just testing 1 2")
    def   test_text_content(self) :
        post= Post.objects.get(id=1) 
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name,"Just testing 1 2")

class HomePageViewTest(TestCase):

    def setUp(self):
        Post.objects.create(text="Just testing 1 2")   
            
    def test_url_exist_in_right_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code,200)

    def test_url_by_name(self):
        resp = self.client.get(reverse('home')) 
        self.assertEqual(resp.status_code,200)

    def view_uses_correct_template(self):
        resp = self.client.get(reverse('home')) 
        self.assertEqual(resp.status_code,200)
        self.assertTemplateUsed(resp,'home.html')
