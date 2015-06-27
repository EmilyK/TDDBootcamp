from django.conf.urls import patterns, include, url
from django.contrib import admin
from app.views.create_post import CreatePost
from app.views.show_post import ShowPost

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^posts/new/$', CreatePost.as_view(), name='new_post_path'),
    url(r'^posts/$', CreatePost.as_view(), name='create_post_path'),
    url(r'^posts/(?P<pk>[-\d]+)/$', ShowPost.as_view(), name='show_post_path'),
)
