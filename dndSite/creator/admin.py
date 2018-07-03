from django.contrib import admin

from .models import Character, Race, BaseChrClass, MagicChr

# Register your models here.

admin.site.register(Character)
admin.site.register(Race)
admin.site.register(BaseChrClass)
admin.site.register(MagicChr)

