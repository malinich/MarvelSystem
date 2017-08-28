from django.conf.urls import  url
from MarvelComixStore import views

urlpatterns = [
    url(r'^marvel/(?P<ean>[0-9]{13})',views.ComixView.as_view()),
    url(r'^marvel',views.Search.as_view()),
    url(r'^get_years',views.get_years.as_view()),
    url(r'^get_tags',views.get_tags.as_view()),
    url(r'^',views.Index.as_view())
]
