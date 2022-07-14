from django.contrib import admin
from .models import link


# Register your models here.
class linkupDB(admin.ModelAdmin):
    list_display = [
        "target_url","description","identifier", "author", "Created_date","active"
    ]
admin.site.register(link, linkupDB)