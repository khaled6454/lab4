from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:price>/", views.tax, name="tax"),
    path("<int:price>/taxrate/", views.taxrate, name="taxrate"),

]