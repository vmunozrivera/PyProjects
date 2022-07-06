from django.contrib import admin

from .models import Movie, Director


class MovieInLine(admin.StackedInline):
    model = Movie
    extra = 1


class DirectorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ('first_name', 'last_name', 'bio', 'image')}),
        ('Dates', {
            'fields': ('birth', 'dead'),
            'classes': 'collapse'
        }),
    ]
    inlines = [MovieInLine]


admin.site.register(Director, DirectorAdmin)
