"""petsProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from PUPG import views as PUPG_views 

urlpatterns = [
    path('admin/', admin.site.urls),
]


urlpatterns += [
    path('PUPG/', include('PUPG.urls')),
]

urlpatterns += [
    path('', RedirectView.as_view(url='/PUPG/')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#urlpatterns += url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
 #           'document_root': settings.MEDIA_ROOT,
 #       }),
   
urlpatterns += [path("accounts/", include("django.contrib.auth.urls"))]

urlpatterns += [url(r'^registration/$', PUPG_views.registration, name='registration')]

urlpatterns += [url(r'^updateprofile/$', PUPG_views.update_profile, name='updateprofile')]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
