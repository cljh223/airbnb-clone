from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    fieldsets = (
        ("Basic Info", {"fields": ("name", "description", "country", "city", "price")}),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guest", "beds", "bedrooms", "baths")}),
        ("More About the Space", {"fields": ("amenities", "facilities", "house_rule")}),
        ("Last Details", {"fields": ("host",)}),
    )
    list_display = (
        "name",
        "description",
        "country",
        "city",
        "price",
        "guest",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    ordering = ("name", "price")

    list_filter = (
        "instant_book",
        "host__superhost",
        "country",
        "city",
        "room_type",
        "amenities",
        "facilities",
        "house_rule",
    )

    search_fields = ("=city", "^host__username")

    filter_horizontal = ("amenities", "facilities", "house_rule")

    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("__str__", "get_thumnail")

    def get_thumnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}""/>')

    get_thumnail.short_description = "Thumbnail"

