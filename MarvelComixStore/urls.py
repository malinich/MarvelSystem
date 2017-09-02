from django.conf.urls import  url
from MarvelComixStore import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^marvel/(?P<ean>[0-9]{13})',views.ComicsView.as_view()),
    url(r'^marvel',views.Search.as_view(),name='marvel'),
    url(r'^comics/(?P<username>\w+)',views.Comics.as_view(),name='comics'),
    url(r'^get_years',views.get_years.as_view()),
    url(r'^get_added',views.get_added),
    url(r'^get_tags',views.get_tags.as_view()),
    url(r'^auth',auth_views.login, {'template_name': 'auth.html'}, name='login'),
    url(r'^logout',auth_views.logout,{'next_page': '/marvel'}),
    url(r'^add/(?P<ean>[0-9]{13})',views.add),
    url(r'^delete/(?P<ean>[0-9]{13})',views.delete),
    url(r'^master',views.Master.as_view(), name='master')
    #url(r'^',views.Index.as_view()),

]
