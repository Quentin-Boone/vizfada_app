from django.urls import path

from . import views

app_name = 'metadata'
urlpatterns = [
    path('', views.index, name='index'),
    path('all/', views.metadata, name="metadata"),
    path('fields/', views.fields, name='fields'),
    path('table/', views.table, name='table'),
    path('groups/', views.groups, name='groups')
]
