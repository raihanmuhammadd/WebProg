from django.urls import path
from webpem import views
urlpatterns = [
    path("", views.index, name='index'),
]