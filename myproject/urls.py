from django.conf.urls import patterns, include, url
from django.contrib import admin
from cms import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^cms/$','cms.views.informacion'),
    url(r'^cms/(\w+)/$', 'cms.views.buscar'),
    url(r'^admin/', include(admin.site.urls)),
)
