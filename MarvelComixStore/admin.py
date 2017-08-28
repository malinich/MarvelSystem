from django.contrib import admin
from MarvelComixStore import models

admin.site.register(models.Comix)
admin.site.register(models.Tag)
admin.site.register(models.Customer)

# Register your models here.
