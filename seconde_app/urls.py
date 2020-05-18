from django.urls import path
from seconde_app import views

urlpatterns = [
    path('',views.home,name="home"),
    path('add',views.add,name="add")
]