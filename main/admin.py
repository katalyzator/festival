from django.contrib import admin

from .models import News, NewsImage


# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description']
    list_display = ['title']
    list_filter = ['title', 'timestamp']

    readonly_fields = ['updated', 'timestamp']
    prepopulated_fields = {"slug": ("title",)}

    class Meta:
        model = News


admin.site.register(News)

admin.site.register(NewsImage)
