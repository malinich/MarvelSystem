from django.db import models
from django.utils import timezone
from rest_framework import serializers
from django.contrib.auth.models import User

class Tag(models.Model):
    name=models.CharField(max_length=20,verbose_name="Тег")

    def __str__(self):
        return str(self.name)



class Comix(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    description = models.TextField(verbose_name="Описание")
    date = models.DateField(default=timezone.now,db_index=True,editable=True, verbose_name="Дата выхода")
    ean = models.CharField(max_length=13,unique=True,primary_key=True, verbose_name="EAN")
    cover = models.ImageField(verbose_name="Обложка")
    tags = models.ManyToManyField(verbose_name="Теги",to=Tag)


    def getShortDesc(self):
        i=500
        while str(self.description)[i]!=" ":
            i=i+1
        return str(self.description)[:i]+"..."

    def getYear(self):
        return self.date.year.numerator;

    def __str__(self):
        return self.name;


class Customer(User):
    comixlist=models.ManyToManyField(to=Comix)

    def __str__(self):
        return self.USERNAME_FIELD


class ComixSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comix
        fields=('name','description','date','ean','cover','tags')

