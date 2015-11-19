from django.conf.urls import patterns, include, url
from django.contrib import admin
from mybooks import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myMVC.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.welcome),
    url(r'^search/$',views.searchlist),
    url(r'^delete/$',views.deleter),
    url(r'^detail/$',views.information),
)