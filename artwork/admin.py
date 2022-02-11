from django.contrib import admin
from .models import Artwork, Category
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {
        'slug': ('name',)
    }


@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ['art', 'title', 
                    'description', 'creator', 'created_at']

    list_filter = ['art','creator' ,'created_at']
    prepopulated_fields = {
        'slug':('title',)
    }