from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('cart/', views.cart, name="cart"),
    path('add-to-cart/<int:food_id>/', views.add_to_cart, name="add_to_cart"),
    path('remove-from-cart/<int:cart_id>/', views.remove_from_cart, name="remove_from_cart"),
    path('increase-quantity/<int:cart_id>/', views.increase_quantity, name='increase_quantity'),
    path('decrease-quantity/<int:cart_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('place-order/', views.place_order, name="place_order"),
    path('tracking/', views.tracking, name='tracking'),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("profile/", views.profile, name="profile"),
    path('order-success/', views.order_success, name='order_success'),
    path('orders/', views.orders, name="orders"),
    path('logout/',views.logout,name='logout'),
    path('wishlist/<int:food_id>/', views.add_to_wishlist, name="add_to_wishlist"),
    path("wishlist/", views.wishlist, name="wishlist"),
    path(
    'remove-from-wishlist/<int:wishlist_id>/',
    views.remove_from_wishlist,
    name='remove_from_wishlist'
),
   path('review/<int:food_id>/', views.add_review, name='add_review'),
    ]