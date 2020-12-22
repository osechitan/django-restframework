from django.contrib import admin

from .models import Novel


class NovelModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at', 'revision_id')
    ordering = ('created_at',)


admin.site.register(Novel, NovelModelAdmin)
