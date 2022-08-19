from django.contrib import admin
from .models import Todowoo

class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Todowoo, TodoAdmin)
