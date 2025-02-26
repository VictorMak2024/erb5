from django.urls import path
from . import views #import views.py

# views <- f()
# models <- database schema
# urls <- paths
# Apps <- object

# ''<- url endpoint, views<- function , in this case, index fucnction in views; '' is endpoint
urlpatterns = [
    path('',views.index, name='index'),
    path('about',views.about, name='about'),
]
