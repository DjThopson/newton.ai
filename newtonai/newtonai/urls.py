
from django.conf.urls import patterns, include, url
from django.contrib import admin
from post import views as main_views
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main_views.HomePageView.as_view(), name='home'),
    url(r'^recommend/', main_views.HomePageView.post, name='recommend'),

]

urlpatterns += patterns('',
    url(r'^pic_post/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            }),
)
