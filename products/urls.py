from django.urls import path

urlpatterns = [
    path(''),
    path('<id>/'),
    path('categories/'),
    path('categories/<id>/')
]