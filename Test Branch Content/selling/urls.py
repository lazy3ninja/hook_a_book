from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_create_view, name = "selling")
]
