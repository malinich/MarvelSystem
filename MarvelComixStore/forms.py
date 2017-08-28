from django.forms import Form
from django import forms
from django.utils import timezone
from MarvelComixStore.models import Comix,Tag

class searchForm(Form):
    keywords = forms.CharField(max_length=100, label="Ключевые слова или тэги", required=False)
    iquery = []
    for i in Comix.objects.all():
        iquery.append(i.getYear())
    iset=set(iquery)
    iquery_choices = [(0, '----------')] + [(i, i) for i in iset]
    year=forms.ChoiceField(iquery_choices, label='Год выпуска',required=False)
    iquery=Tag.objects.values_list('name',flat=True).distinct()