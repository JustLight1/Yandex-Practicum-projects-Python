from django.contrib import admin

from .models import Category, Comment, Genre, Review, Title


class TitleAdmin(admin.ModelAdmin):
    list_display: tuple = ('pk', 'name', 'year', 'category')
    list_editable: tuple = ('category',)
    search_fields: tuple = ('name',)
    empty_value_display: str = '-пусто-'


class CategoryAdmin(admin.ModelAdmin):
    list_display: tuple = ('pk', 'name', 'slug')
    search_fields: tuple = ('name',)
    empty_value_display: str = '-пусто-'


class GenreAdmin(admin.ModelAdmin):
    list_display: tuple = ('name', 'slug')
    search_fields: tuple = ('name',)
    empty_value_display: str = '-пусто-'


class ReviewAdmin(admin.ModelAdmin):
    list_display: tuple = ('title', 'text', 'score')
    empty_value_display: str = '-пусто-'


class CommentAdmin(admin.ModelAdmin):
    list_display: tuple = ('id', 'text')
    empty_value_display: str = '-пусто-'


admin.site.register(Title, TitleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
