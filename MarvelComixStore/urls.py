from django.conf.urls import  url
from MarvelComixStore import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^marvel/(?P<ean>[0-9]{13})',views.ComixView.as_view()),
    url(r'^marvel',views.Search.as_view(),name='marvel'),
    url(r'^comics/(?P<username>\w+)',views.Comics.as_view(),name='comics'),
    url(r'^get_years',views.get_years.as_view()),
    url(r'^get_tags',views.get_tags.as_view()),
    url(r'^auth',auth_views.login, {'template_name': 'auth.html'}, name='login'),
    url(r'^logout',views.LogOut),
    url(r'^add/(?P<ean>[0-9]{13})',views.add)
    #url(r'^',views.Index.as_view()),

]
