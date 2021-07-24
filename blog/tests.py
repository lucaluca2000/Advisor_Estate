from rest_framework import response
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status
#automated
#new / blank db
from .models import Article,Category
User=get_user_model()
class ArticlesPostAPITestCase(APITestCase):
    def setUp(self):
        user=User.objects.create(username='testaliuser',email='test@test.com')
        user.set_password('flsrgvjsdf')
        user.save()
        article_post=Article.objects.create(title='New title',author=user,slug='new',description='gfdsgg',status='true',)
        
    def test_single_user(self):
        user_count=User.objects.count()
        self.assertEqual(user_count,1)

    def test_single_post(self):
        post_count=User.objects.count()
        self.assertEqual(post_count,1)


    # def test_get_item(self):
    #     data = {}
    #     url = api_reverse("blog-home")
    #     response = self.client.get(url,data,format='json')

    #     self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_get_list(self):
        data = {}
        url = api_reverse("blog-list-article")
        response = self.client.get(url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        # print(response.data)



    def test_post_item(self):
        data = {'title':'New title','author':'user','slug':'new','description':'gfdsgg','status':'True',}
        url = api_reverse("blog-list-article")
        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)


class CategoryPostAPITestCase(APITestCase):
    def setUp(self):
        user=User.objects.create(username='testaliuser',email='test@test.com')
        user.set_password('flsrgvjsdf')
        user.save()
        article_post=Category.objects.create(title='New title',slug='new',status='True',)
        
    def test_single_user(self):
        user_count=User.objects.count()
        self.assertEqual(user_count,1)

    def test_single_post(self):
        post_count=User.objects.count()
        self.assertEqual(post_count,1)


    # def test_get_item(self):
    #     data = {}
    #     url = api_reverse("blog-home")
    #     response = self.client.get(url,data,format='json')

    #     self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_get_list(self):
        data = {}
        url = api_reverse("blog-list-category")
        response = self.client.get(url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        # print(response.data)



    def test_post_item(self):
        data = {'title':'New title','slug':'new','status':'True',}
        url = api_reverse("blog-list-category")
        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
