# Project 3

- Complete the Menu, Adding Items, and Registration/Login/Logout steps.

## The menu:

Since i was still unsure off how the relationship between each table worked and how foreign key would take place. I decided to treat each model in the menu as seperate entities.

```html
class Regular_pizza(models.Model):
	item = models.CharField(max_length = 64)
	small = models.FloatField(default = 0)
	large = models.FloatField(default = 0)

	def __str__(self):
		return self.item

class Sicilian_pizza(models.Model):
	item = models.CharField(max_length = 64)
	small = models.FloatField(default = 0)
	large = models.FloatField(default = 0)

	def __str__(self):
		return self.item

class Topping(models.Model):
	name = models.CharField(max_length = 64)

	def __str__(self):
		return self.name

```

## Adding items:

I added items to the database using the interface provided by django, which can be seen in the video

## Registration/Login/Logout:

I followed the django video tutorial and ended up with something quite similar:

```html
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

```

- Complete the Shopping Cart and Placing an Order steps.

## Shopping Cart:

The idea was very simple. I wanted to create a pool to place all of the items in. Then i would filter out the items so that the users would not be able to see each others cart item

```html
for cart in carts:
	if cart.user == request.user.username:
```
See the video for more detail in-depth of how i solved some of the other problems

## Place an Order:

I created a seperate model to insert all of the orders. Whenever the user placed an order, the information would be added to the database and the cart items related to the order made would be deleted.

- Complete the Viewing Orders and Personal Touch steps.

## Viewing Orders:

I created a seperate html file where only users with superuser status would be able to access.

## Personal Touch:

Each order comes with a ready state. Either the order is ready or not (True or False). The admin/superuser would be able to change the state of an order in the "Viewing order page".



