from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_didactics.views.home', name='home'),
    # url(r'^django_didactics/', include('django_didactics.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


# if settings.DEBUG:
#     urlpatterns = patterns('',
#     url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
#         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
# 	url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
# 		{'document_root': settings.STATIC_ROOT}),
#     url(r'', include('django.contrib.staticfiles.urls')),
# ) + urlpatterns
