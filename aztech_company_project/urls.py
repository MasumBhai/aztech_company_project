"""django_web_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls import include, url
import debug_toolbar

admin.site.site_header = "Aztech Valley"
admin.site.site_title = "Aztech site maintainance"
admin.site.index_title = "Welcome Admin"

urlpatterns = [
                  # url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
                  path('', RedirectView.as_view(url='home/', permanent=True)),
                  path('', include('aztech.urls')),
                  path('admin/', admin.site.urls),
                  path('__debug__/', include(debug_toolbar.urls)),
                  path('summernote/', include('django_summernote.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
                       path('__debug__/', include(debug_toolbar.urls)),
                   ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
