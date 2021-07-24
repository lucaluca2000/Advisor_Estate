import re
from django.db.models import query
from rest_framework import generics, mixins, serializers
from .models import Article,Category
from .serializers import ArticleSeriallizer,CategorySeriallizer
from .permissions import IsOwnerOrReadOnly,IsSuperUserOrStaffReadOnly
from django.db.models import Q
from django.shortcuts import get_object_or_404




class ArticleAPIView(mixins.CreateModelMixin,generics.ListAPIView):
    lookup_field='pk'
    serializer_class=ArticleSeriallizer
    def get_queryset(self):
        qs=get_object_or_404(Article.objects.published())

        query=self.request.GET.get("q")
        if query is not None:
            qs=qs.filter(Q(title__icontains=query)|Q(description__icontains=query)|
            Q(author__icontains=query)|Q(category__icontains=query)).distinct()
        return qs
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    def get_serializer_context(self):
        return {"request":self.request}
    # def put(self,request,*args,**kwargs):
    #     return self.update(request,*args,**kwargs)
         
    # def patch(self,request,*args,**kwargs):
    #     return self.update(request,*args,**kwargs)
 


class ArticlesPost(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=ArticleSeriallizer
    permission_classes=[IsSuperUserOrStaffReadOnly, ]

    lookup_field='pk'
    def get_queryset(self):
        qs=get_object_or_404(Article.objects.published())

        return qs
    
    def get_serializer_context(self):
        return {"request":self.request}




class CategoryAPIView(mixins.CreateModelMixin,generics.ListAPIView):
    lookup_field='pk'
    serializer_class=CategorySeriallizer
    def get_queryset(self):
        qs=get_object_or_404(Category.objects.active())


        query=self.request.GET.get("q")
        if query is not None:
            qs=qs.filter(Q(title__icontains=query)).distinct()
        return qs
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    # def put(self,request,*args,**kwargs):
    #     return self.update(request,*args,**kwargs)
         
    # def patch(self,request,*args,**kwargs):
    #     return self.update(request,*args,**kwargs)
 
    def get_serializer_context(self):
        return {"request":self.request}
 


class CategoriesPost(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=CategorySeriallizer
    # permission_classes=[IsSuperUserOrStaffReadOnly, ]

    lookup_field='pk'
    def get_queryset(self):
        qs=get_object_or_404(Category.objects.active())

        return qs

    
    def get_serializer_context(self):
        return {"request":self.request}
