from . import views
from django.urls import path

app_name = "experiment"

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:id>', views.get_experiment_files, name="experiment_files")
]
