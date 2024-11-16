from django.contrib import admin
from .models import Categoria, Post, Comment

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)