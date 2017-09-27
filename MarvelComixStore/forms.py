from django.forms import Form
from django import forms

from MarvelComixStore.models import Comix, Tag


class searchForm(Form):
    keywords = forms.CharField(max_length=100, label="Ключевые слова или тэги", required=False)
    year = forms.ChoiceField([], label='Год выпуска', required=False)
    iquery = Tag.objects.values_list('name', flat=True).distinct()

    def __init__(self, *args, **kwargs):
        super(searchForm, self).__init__(*args, **kwargs)

        self.fields['year'].choices = self.populate_years()

    def populate_years(self):
        iquery = []
        for i in Comix.objects.all():
            iquery.append(i.getYear())
        iset = set(iquery)
        iquery_choices = [(0, '----------')] + [(i, i) for i in iset]
        return iquery_choices
