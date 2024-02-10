from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('hello/', views.sayHello) # Use path to create a URL pattern object
]
