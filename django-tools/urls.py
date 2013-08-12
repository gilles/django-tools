from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

                       url(r'^/?$', 'common.views.home', name='home'),

                       url(r'^sprints/', include('sprints.urls', namespace='sprints')),

                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^admin/', include(admin.site.urls)),
)
