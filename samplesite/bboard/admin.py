from django.contrib import admin

from .models import Bb, Rubric


class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'rubric', 'content', 'price', 'published')
    list_display_links = ('title',)
    list_per_page = 100
    search_fields = ('title', 'content',)
    search_help_text = "Введите название объявления"


admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)








