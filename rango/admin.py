from django.contrib import admin
from rango.models import Category, Page


# Customise the admin interface so that
# it automatically prepopulates the slug field
# as you type in the category name.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page)