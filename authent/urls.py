from django.urls import path
from . import views
urlpatterns=[
    path('',views.Login_,name='login'),
    path('register',views.Register_,name='register'),
    path('logout',views.Logout_,name='logout'),
    path('profile',views.profile,name='profile'),
]