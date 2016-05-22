from django.contrib import admin
from .models import Category, Tag, Post

class CategoryModelAdmin(admin.ModelAdmin):
    list_display = [ "name", "slug", "description"]
    list_filter = ["name", "description"]
    search_fields = ['name', "slug", "description"]
    class Meta:
        model = Category

# Register your Category
admin.site.register(Category, CategoryModelAdmin)

class TagModelAdmin(admin.ModelAdmin):
    list_display = [ "name", "slug", "description"]
    list_filter = ["name", "description"]
    search_fields = ['name', "slug", "description"]
    class Meta:
        model = Tag

# Register your Tag
admin.site.register(Tag, TagModelAdmin)

class PostModelAdmin(admin.ModelAdmin):
    list_display = [ "title", "description", "pub_date"]
    list_filter = ["title", "description"]
    search_fields = ['title', "description"]
    class Meta:
        model = Post

# Register your Post
admin.site.register(Post, PostModelAdmin)