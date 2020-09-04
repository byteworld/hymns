from django.contrib import admin
from .models import Hymn

class HymnAdmin(admin.ModelAdmin):
    list_display = ('id', 'Ename', 'Elyrics', 'id2', 'Yname', 'time', 'meter', 'Ylyrics')


admin.site.register(Hymn, HymnAdmin)
