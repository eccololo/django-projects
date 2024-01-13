from django.contrib import admin
from .models import List


class ListAdmin(admin.ModelAdmin):
    fields = ["item", "completed"]
    list_filter = ["completed"]
    search_fields = ["item"]


admin.site.register(List, ListAdmin)
