from django.contrib import admin
from .models import Urls



class UrlsAdmin(admin.ModelAdmin):
    list_display = ('short_id', 'httpurl', 'date')
    ordering = ('-date',)


admin.site.register(Urls, UrlsAdmin)