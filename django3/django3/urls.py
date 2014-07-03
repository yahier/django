from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
     ('^hello', ya),
                       ('error.', error),
                        ('html.', html),
                       ('time/$', current_datetime),
                       (r'^time/plus/(\d+)/$', hours_ahead),
)
