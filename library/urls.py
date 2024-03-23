from django.urls import path
from . import views
urlpatterns = [
    path('', views.main, name="main"),
    path('base/', views.base, name="base"),
    path('books/', views.books, name="books"),
    path('borrowed/', views.borrowed, name="borrowed"),
    path('books/details',views.details, name="details"),
    path('borrowed/details', views.details, name="details"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('adminpage', views.adminpage, name="adminpage"),
    path('addbook', views.addbook, name="addbook"),
]
