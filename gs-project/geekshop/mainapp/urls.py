from django.urls import path
import mainapp.views as mainapp
from django.urls import re_path

app_name = 'mainapp'
urlpatterns = [
    # path('', mainapp.products, name='index'),
    # path('category/<int:pk>/', mainapp.products, name='category'),
    # path('product/<int:pk>/', mainapp.product, name='product'),
    # path('category/<int:pk>/page/<int:page>/', mainapp.products, name='page'),

    re_path(r'^$', mainapp.products, name='index'),
    # re_path(r'^contact/', mainapp.contact, name='contact'),
    re_path(r'^category/(?P<pk>\d+)/$', mainapp.products, name='category'),
    re_path(r'^product/(?P<pk>\d+)/$', mainapp.product, name='product'),
    re_path(r'^category/(?P<pk>\d+)/page/(?P<page>\d+)/$', mainapp.products, name='page'),
]

