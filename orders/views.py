from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Order, Cart, Regular_pizza, Sicilian_pizza, Topping, Sub, Pasta, Salad, Dinner

total = 0
description = ""
ordered = False

def add(request, item):
	#if not request.POST.get("size"):
		#return HttpResponseRedirect(reverse("cart"))
	#else:
		#price = request.POST["size"]
		#cart = Cart(user = request.user, item = item, price = price)
		#cart.save()
		#return HttpResponseRedirect(reverse("cart"))

	price = request.POST["size"]
	cart = Cart(user = request.user, item = item, price = price)
	cart.save()
	return HttpResponseRedirect(reverse("cart"))

def remove(request, id):
	Cart.objects.filter(id=id).delete()
	return HttpResponseRedirect(reverse("cart"))

def update(request, id):
	order = Order.objects.get(id=id)
	if order.finished:
		order.finished = False
	else:
		order.finished = True

	order.save()
	return HttpResponseRedirect(reverse("manage"))

def manage(request):
	context = {
		"user": request.user,
		"orders": Order.objects.all()
	}
	return render(request, "orders/manage.html", context)

def order(request):
	global ordered
	user = request.user.username
	order = Order(user=user, description=description, price=total)
	order.save()

	ordered = True

	return HttpResponseRedirect(reverse("cart"))

def cart(request):
	global total #global keyword is used to allow for modification for global scoped variables
	global description
	global ordered

	total = 0
	description = ""
	cartlist = []

	carts = Cart.objects.all()

	if ordered:
		Cart.objects.filter(user=request.user.username).delete()
		ordered = False

	for cart in carts:
		if cart.user == request.user.username:
			cartlist.append(cart)
			description+=str(cart) + ", "
			total += cart.price

	context = {
		"user": request.user,
		"carts": cartlist,
		"description": description,
		"total": total,
		"regular": Regular_pizza.objects.all(),
		"sicilian": Sicilian_pizza.objects.all(),
		"toppings": Topping.objects.all(),
		"subs": Sub.objects.all(),
		"pastas": Pasta.objects.all(),
		"salads": Salad.objects.all(),
		"dinners": Dinner.objects.all()
	}

	return render(request, "orders/order.html", context)

def pending(request):
	context = {
		"user": request.user,
		"orders": Order.objects.all()
	}
	return render(request, "orders/pending.html", context)

# Create your views here.
def index(request):
	if not request.user.is_authenticated:
		return render(request, "orders/index.html", {"message": None})

	elif request.user.is_superuser:
		return HttpResponseRedirect(reverse("manage"))
	else:
		return HttpResponseRedirect(reverse("pending"))

def login_view(request):
	user = request.POST["user"]
	password = request.POST["password"]

	#return HttpResponse(email)
	#return HttpResponse(password)

	user = authenticate(request, username=user, password=password)
		
	if user is not None:
		login(request, user)
		if user.is_superuser:
			return HttpResponseRedirect(reverse("manage"))
		else:
			return HttpResponseRedirect(reverse("index"))
	else:
		return render(request, "orders/index.html", {"message": "Invalid credentials"})

def logout_view(request):
	logout(request)
	return render(request, "orders/index.html", {"message": "Logged out"})

def register_view(request):
	return render(request, "orders/register.html")

def register_auth(request):
	user = request.POST["user"]
	email = request.POST["email"]
	password = request.POST["password"]

	if not user or not email or not password:
		return render(request, "orders/register.html", {"message": "Please fill in all the fields"})
	user = User.objects.create_user(user, email, password)
	return HttpResponseRedirect(reverse("index"))

