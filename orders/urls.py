from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name="register"),
    path("register_auth", views.register_auth, name="register_auth"),
    path("add/<str:item>/", views.add, name="add"),
    path("cart", views.cart, name="cart"),
    path("order", views.order, name="order"),
    path("remove/<int:id>", views.remove, name="remove"),
    path("manage", views.manage, name="manage"),
    path("pending", views.pending, name="pending"),
    path("update/<int:id>", views.update, name="update")
]
