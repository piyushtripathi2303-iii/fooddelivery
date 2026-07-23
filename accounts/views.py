from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Food, Cart, Order, Wishlist,Review


def home(request):

    # Login
    if request.method == "POST":
        name = request.POST["name"]
        password = request.POST["password"]

        try:
            user = User.objects.get(name=name, password=password)
            request.session["user_id"] = user.id
            request.session["user_name"] = user.name
            return redirect("home")

        except User.DoesNotExist:
            return HttpResponse("Invalid Username or Password")

    # Check Login
    if "user_id" not in request.session:
        return render(request, "accounts/login.html")

    # Search
    search = request.GET.get("search")
    category = request.GET.get("category")
    sort = request.GET.get("sort")


    if category:
     foods = Food.objects.filter(category=category)
    elif search:
     foods = Food.objects.filter(name__icontains=search)
    else:
     foods = Food.objects.all()
     if sort == "low":
      foods = foods.order_by("price")

     elif sort == "high":
      foods = foods.order_by("-price")

    wishlist = Wishlist.objects.values_list("food_id", flat=True)
    popular_foods = Food.objects.filter(rating__gte=4.5)
    return render(request, "accounts/home.html", {
        "foods": foods,
        "wishlist": wishlist,
        "popular_foods":popular_foods,
    })


def register(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]

        User.objects.create(
            name=name,
            email=email,
            password=password
        )

        return HttpResponse("Registration Successful")

    return render(request, "accounts/register.html")


def logout(request):
    request.session.flush()
    return redirect("home")


def add_to_cart(request, food_id):
    food = Food.objects.get(id=food_id)
    Cart.objects.create(food=food)
    return redirect("cart")


def cart(request):

    if request.method == "POST":
        coupon = request.POST.get("coupon")

        if coupon == "SAVE50":
            request.session["discount"] = 50
        else:
            request.session["discount"] = 0

    cart_items = Cart.objects.all()

    total = 0
    for item in cart_items:
        total += item.food.price * item.quantity

    delivery = 40

    if total >= 299:
        delivery = 0

    discount = request.session.get("discount", 0)

    grand_total = total + delivery - discount

    return render(request, "accounts/cart.html", {
        "cart_items": cart_items,
        "total": total,
        "delivery": delivery,
        "discount": discount,
        "grand_total": grand_total,
    })


def remove_from_cart(request, cart_id):
    item = Cart.objects.get(id=cart_id)
    item.delete()
    return redirect("cart")
def increase_quantity(request, cart_id):
    item = Cart.objects.get(id=cart_id)
    item.quantity += 1
    item.save()
    return redirect("cart")


def decrease_quantity(request, cart_id):
    item = Cart.objects.get(id=cart_id)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect("cart")


def place_order(request):

    print("METHOD =", request.method)

    if request.method == "GET":
        print("PAYMENT PAGE")
        return render(request, "accounts/payment.html")

    elif request.method == "POST":
        print("PROCESSING PAGE")
        return render(request, "accounts/processing.html")
    
def order_success(request):

    cart_items = Cart.objects.all()

    for item in cart_items:
        Order.objects.create(
            food=item.food
        )

    cart_items.delete()

    return render(request, "accounts/order_success.html")


def orders(request):
    all_orders = Order.objects.all()

    return render(request, "accounts/orders.html", {
        "orders": all_orders
    })


def add_to_wishlist(request, food_id):
    food = Food.objects.get(id=food_id)

    item = Wishlist.objects.filter(food=food).first()

    if item:
        item.delete()
    else:
        Wishlist.objects.create(food=food)

    return redirect("home")


def wishlist(request):
    items = Wishlist.objects.all()

    return render(request, "accounts/wishlist.html", {
        "items": items
    })

def add_review(request, food_id):
    if request.method == "POST":
        food = Food.objects.get(id=food_id)
        user = User.objects.get(id=request.session["user_id"])

        rating = request.POST["rating"]
        review = request.POST["review"]

        Review.objects.create(
            food=food,
            user=user,
            rating=rating,
            review=review
        )

    return redirect("home")
def remove_from_wishlist(request, wishlist_id):
    item = Wishlist.objects.get(id=wishlist_id)
    item.delete()
    return redirect("wishlist")

def tracking(request):
    return render(request, "accounts/tracking.html")
def about(request):
    return render(request, "accounts/about.html")


def contact(request):
    return render(request, "accounts/contact.html")
def profile(request):
    user = User.objects.get(id=request.session["user_id"])

    if request.method == "POST":
        user.name = request.POST["name"]
        user.email = request.POST["email"]
        user.phone = request.POST["phone"]
        user.address = request.POST["address"]
        user.save()

        request.session["user_name"] = user.name

        return redirect("profile")

    orders = Order.objects.count()
    wishlist = Wishlist.objects.count()
    reviews = Review.objects.count()

    return render(request, "accounts/profile.html", {
        "user": user,
        "orders": orders,
        "wishlist": wishlist,
        "reviews": reviews,
    })
