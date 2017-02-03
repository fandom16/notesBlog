# Adding commentaries
# Ajout de commentaire


from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/nouvelle_note/$', views.post_new, name='post_new'),
]
