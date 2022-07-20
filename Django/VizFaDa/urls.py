"""VizFaDa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
import debug_toolbar

from VizFaDa.views import index as i, csrf

urlpatterns = [
    path("", i.index, name='index'),
    path('data/', include('data.urls', namespace='data')),
    path('heatmap/', include('heatmap.urls', namespace='heatmap')),
    path('epistack/', include('epistack.urls', namespace='epistack')),
    path('experiment/', include('experiment.urls', namespace='experiment')),
    path('metadata/', include('metadata.urls', namespace='metadata')),
    path('correlation/', include('correlation.urls', namespace='correlation')),
    path('csrf', csrf.get_csrf, name="csrf"),
    path("__debug__/", include(debug_toolbar.urls))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
