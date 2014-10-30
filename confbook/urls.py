from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^meetingrooms/', include('meeting.urls', namespace='meeting')),
    url(r'^admin/', include(admin.site.urls)),
)
