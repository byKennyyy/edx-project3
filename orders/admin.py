from django.contrib import admin

from .models import Order, Cart, Regular_pizza, Sicilian_pizza, Topping, Sub, Pasta, Salad, Dinner

# Register your models here.
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Regular_pizza)
admin.site.register(Sicilian_pizza)
admin.site.register(Topping)
admin.site.register(Sub)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(Dinner)