import models
from django.contrib import admin
from .models import Category, Tag, Post

class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "description"]
    list_filter = ["name", "description"]
    search_fields = ["name", "slug", "description"]
    list_display_links = ["name"]
    class Meta:
        model = Category

# Register your Category
admin.site.register(Category, CategoryModelAdmin)

class TagModelAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "description"]
    list_filter = ["name", "description"]
    search_fields = ["name", "slug", "description"]
    list_display_links = ["name"]
    class Meta:
        model = Tag

# Register your Tag
admin.site.register(Tag, TagModelAdmin)

class CategoryToPostInline(admin.TabularInline):
    model = models.CategoryToPost
    extra = 1

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "pub_date"]
    list_filter = ["title", "description"]
    search_fields = ["title", "description"]
    list_display_links = ["title"]
    fields = ('title', 'featured_photo', 'description', 'status', 'pub_date', 'tag',)
    inlines = [CategoryToPostInline]

    class Meta:
        model = Post

# Register your Post
admin.site.register(Post, PostModelAdmin)
