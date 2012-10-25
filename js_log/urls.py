from django.conf.urls.defaults import *

urlpatterns = patterns('js_log.views',
    url(r'^log_error/$', 'log_error', name='js_log_error'),
)
