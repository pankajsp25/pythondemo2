from django.contrib import admin

# Register your models here.

from master import models

admin.site.register(models.CannabisSmoke)
admin.site.register(models.Religion)
admin.site.register(models.Hobbies)
admin.site.register(models.Education)
