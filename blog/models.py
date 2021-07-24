from django.db import models
from django.utils import timezone
from account.models import User
from django.urls import reverse
from rest_framework.reverse import reverse as api_reverse
from extensions.utils import jalali_converter
# my managers
class ArticleManager(models.Manager):
	def published(self):
		return self.filter(status='p')


class CategoryManager(models.Manager):
	def active(self):
		return self.filter(status=True)




# Create your models here.
STATUS_CHOICES = (
		('d', 'پیش‌نویس'),		 # draft
		('p', "منتشر شده"),		 # publish
		('i', "در حال بررسی"),	 # investigation
		('b', "برگشت داده شده"), # back
	)
class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name='children', verbose_name="زیردسته")
    title=models.CharField(max_length=200,verbose_name="عنوان")
    slug=models.SlugField(max_length=200,unique=True,verbose_name="آدرس")
    status=models.BooleanField(default=True,verbose_name="وضعیت")
    def __str__(self):
        return self.title
    objects = CategoryManager()

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی ها"
        ordering = ['parent__id','-status']


    def get_api_url(self,request=None):
        return api_reverse("category-home",kwargs={'pk':self.pk},request=request)

class Article(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='articles', verbose_name="نویسنده")
    title=models.CharField(max_length=200,verbose_name="عنوان")
    slug=models.SlugField(max_length=200,unique=True,verbose_name="آدرس")
    description=models.TextField(verbose_name="محتوا")
    publish=models.DateTimeField(default=timezone.now)
    category=models.ManyToManyField(Category,verbose_name="دسته بندی",related_name='articles')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=1,choices=STATUS_CHOICES,verbose_name="وضعیت")
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ['-publish']
    def category_to_str(self):
        return "، ".join([category.title for category in self.category.active()])
    category_to_str.short_description = "دسته‌بندی"

    def jpublish(self):
        return jalali_converter(self.publish)
    jpublish.short_description = "زمان انتشار"


    def get_api_url(self,request=None):
        return api_reverse("blog-home",kwargs={'pk':self.pk},request=request)
    # def get_absolute_url(self):
        # return reverse("model_detail", kwargs={"pk": self.pk})
    objects=ArticleManager()