"""festival URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, patterns, include
from django.contrib import admin
from django.conf.urls.static import static

from festival import settings

urlpatterns = patterns('',
                       url(r'^jet/', include('jet.urls', 'jet')),
                       url(r'^admin/', admin.site.urls),
                       url(r'^$', 'main.views.main', name='main'),
                       url(r'^partners/$', 'main.views.partners_view', name='partners'),
                       url(r'^news/(?P<id>\d+)/$', 'main.views.single', name='single_news'),
                       url(r'^registration/$', 'main.views.registrationView', name='registration'),
                       url(r'^reg/send/$', 'main.views.send_mail', name='send_mail'),
                       url(r'about/$', 'main.views.about_view', name='about'),
                       url(r'reglament/$', 'main.views.reglament_view', name='reglament'),
                       url(r'festival2011/$', 'main.views.coah_view2011', name='festival2011'),
                       url(r'festival2012/$', 'main.views.coah_view2012', name='festival2012'),
                       url(r'festival2013/$', 'main.views.coah_view2013', name='festival2013'),
                       url(r'festival2014/$', 'main.views.coah_view2014', name='festival2014'),
                       url(r'festival2015/$', 'main.views.coah_view2015', name='festival2015'),
                       url(r'aitysh/$', 'main.views.aitysh_view', name='fond_view'),
                       url(r'contacts/$', 'main.views.contacts_view', name='contacts'),
                       url(r'photos2011/$', 'main.views.photos2011_view', name='photos_2011'),
                       url(r'photos2012/$', 'main.views.photos2012_view', name='photos_2012'),
                       url(r'photos2013/$', 'main.views.photos2013_view', name='photos_2013'),
                       url(r'gallery/$', 'main.views.photogallery_view', name='gallery')

                       )

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
