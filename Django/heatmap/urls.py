from . import views
from django.urls import path

app_name = "heatmap"

urlpatterns = [
    path('', views.index, name='index'),
    path('plotly/', views.get_plotly, name="plotly"),
    path('img/', views.get_image, name="img"),
    path('legend/', views.get_legend, name="legend")
]
