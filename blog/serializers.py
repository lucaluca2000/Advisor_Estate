from django.db.models import fields
from rest_framework import request, serializers
from .models import Article,Category

class ArticleSeriallizer(serializers.ModelSerializer):
    url=serializers.SerializerMethodField(read_only=True)
    class Meta():
        model=Article
        fields=[
            'url',
            'id',
            'author',
            'title',
            'slug',
            'description',
            'publish',
            'category',
            'status',
        ]
        read_only_fields=['id']
    def get_url(self,obj):
        request =self.context.get("request")
        return obj.get_api_url(request=request)
    # def validate_title(self,value):
        # qs=Article.objects.filter(title__iexact=value)
        # if self.instance:
        #     qs=qs.exclude(pk=self.instance.pk)
        # if qs.exists():
        #     raise serializers.ValidationError("این عنوان مقاله قبلا اضافه شده است ،‌لطفا دوباره تلاش کنید.")


class CategorySeriallizer(serializers.ModelSerializer):
    url=serializers.SerializerMethodField(read_only=True)
    class Meta():
        model=Category
        fields=[
            'url',
            'id',
            'parent',
            'title',
            'slug',
            'status',

        ]
        read_only_fields=['id']
    def get_url(self,obj):
        request =self.context.get("request")
        return obj.get_api_url(request=request)