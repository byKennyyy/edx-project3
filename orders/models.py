from django.db import models

# Create your models here.

class Order(models.Model):
	user = models.CharField(max_length = 64)
	description = models.CharField(max_length = 999)
	price = models.FloatField()
	finished = models.BooleanField(default = False)

	def __str__(self):
		return self.user

class Cart(models.Model):
	user = models.CharField(max_length = 64, default="guest")
	item = models.CharField(max_length = 64)
	price = models.FloatField()

	def __str__(self):
		return self.item

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

class Sub(models.Model):
	item = models.CharField(max_length = 64)
	small = models.FloatField(default = 0)
	large = models.FloatField(default = 0)

	def __str__(self):
		return self.item

class Pasta(models.Model):
	name = models.CharField(max_length = 64)
	price = models.FloatField(default = 0)

	def __str__(self):
		return self.name

class Salad(models.Model):
	name = models.CharField(max_length = 64)
	price = models.FloatField(default = 0)

	def __str__(self):
		return self.name

class Dinner(models.Model):
	item = models.CharField(max_length = 64)
	small = models.FloatField(default = 0)
	large = models.FloatField(default = 0)

	def __str__(self):
		return self.item

	