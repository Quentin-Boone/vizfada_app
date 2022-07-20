from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'data'
urlpatterns = [
    path('', views.index, name='index'),
    path('all/<path:uri>', views.get_all_files, name="get_all_files"),
    path('list/<path:uri>', views.get_list, name="get_list"),
    path('content/<path:uri>', views.get_file, name="get_file")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

"""
path('img/filter_highlight', views.filter_and_highlight_image_angular, name="filter_highlight_image_angular"),
path('<str:species>/img/<str:size>/filter/highlight', views.filter_and_highlight_image, name="filter_highlight_image"),
path('<str:species>/img/<str:size>/filter', views.filter_image, name="filter_image"),
path('<str:species>/meta/<str:size>/filter/highlight', views.filter_and_highlight_meta, name="filter_highlight_meta"),
path('<str:species>/img/<str:size>', views.image, name="image"),
path('values/<str:species>', views.get_fields_values_species, name='species_fields_values'),
path('values', views.get_all_fields_values, name='all_fields_values')
"""
