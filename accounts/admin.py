from django.utils.html import format_html
from django.contrib import admin
from .models import User, Food, Cart, Order, Wishlist, Review


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "phone")
    search_fields = ("name", "email")


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "food_image",
        "name",
        "category",
        "price",
        "rating",
    )

    list_filter = ("category",)
    search_fields = ("name",)

    def food_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="60" style="border-radius:8px;">',
                obj.image.url
            )
        return "No Image"

    food_image.short_description = "Image"


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("id", "food", "quantity")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "food", "order_date")
    ordering = ("-order_date",)
    date_hierarchy="order_date"


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ("id", "food")


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "food", "user", "rating")
    search_fields = ("food_name", "user_name")
    list_filter=("rating",)