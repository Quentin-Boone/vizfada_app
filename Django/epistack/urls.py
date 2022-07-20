from django.urls import path

from . import views

app_name = 'epistack'
urlpatterns = [
    path('', views.index, name='index'),
    path('filter/', views.filter_epistack, name="filter_epistack"),
    path('imgs/', views.imgs, name="imgs")
]
