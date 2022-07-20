from django.urls import path

from . import views

app_name = 'correlation'
urlpatterns = [
    path('', views.index, name='index'),
    path('jaccard/', views.jaccard, name="jaccard"),
    path('pearson/', views.pearson, name="pearson"),
    path('jaccard_user/', views.jaccard_user, name="jaccard_user")
]
