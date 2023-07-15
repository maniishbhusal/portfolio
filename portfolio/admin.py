from django.contrib import admin
from .models import Portfolio, Blog, Contact, BlogComment


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    prepopulated_fields = {'slug': ('title',)}


# Register your models here.
admin.site.register(Portfolio)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Contact)
admin.site.register(BlogComment)
