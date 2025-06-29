from django.contrib import admin
from django.utils.html import format_html
from .models import Post, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created_at")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)
    list_filter = ("created_at",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "category",
        "published",
        "created_at",
        "featured_image_preview",
    )
    list_filter = ("published", "category", "created_at", "author")
    search_fields = ("title", "content", "excerpt")
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ("author",)
    date_hierarchy = "created_at"
    ordering = ("-created_at",)

    fieldsets = (
        ("Basic Information", {"fields": ("title", "slug", "author", "category")}),
        ("Content", {"fields": ("excerpt", "content", "featured_image")}),
        ("Publication", {"fields": ("published",), "classes": ("collapse",)}),
    )

    def featured_image_preview(self, obj):
        if obj.featured_image:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius: 5px;" />',
                obj.featured_image.url,
            )
        return "No Image"

    featured_image_preview.short_description = "Image Preview"

    def save_model(self, request, obj, form, change):
        if not change:  # If creating new post
            obj.author = request.user
        super().save_model(request, obj, form, change)


# Customize admin site
admin.site.site_header = "MyBlog Administration"
admin.site.site_title = "MyBlog Admin"
admin.site.index_title = "Welcome to MyBlog Administration"
