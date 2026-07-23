from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=50, default="Pizza")
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=4.5)
    image = models.ImageField(upload_to='food_images/', blank=True, null=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.food.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)

    def _str_(self):
        return self.food.name
class Review(models.Model):
     food = models.ForeignKey(Food, on_delete=models.CASCADE)
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     rating = models.IntegerField(default=5)
     review = models.TextField()
     review_date = models.DateTimeField(auto_now_add=True)

def _str_(self):
        return self.food.name + " - " + self.user.name
 