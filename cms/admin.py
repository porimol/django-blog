from django.contrib import admin
from .models import Category, Tag, Post

class CategoryModelAdmin(admin.ModelAdmin):
    list_display = [ "name", "slug", "description"]
    class Meta:
        model = Category

# Register your Category
admin.site.register(Category, CategoryModelAdmin)

class TagModelAdmin(admin.ModelAdmin):
    list_display = [ "name", "slug", "description"]
    class Meta:
        model = Tag

# Register your Tag
admin.site.register(Tag, TagModelAdmin)

class PostModelAdmin(admin.ModelAdmin):
    list_display = [ "title", "description", "pub_date"]
    class Meta:
        model = Post

# Register your Post
admin.site.register(Post, PostModelAdmin)
