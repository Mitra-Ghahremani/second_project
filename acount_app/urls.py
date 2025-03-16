from django.urls import path
from . import views



app_name='acount_app'

urlpatterns=[path('login',views.acount,name="login"),
             path('logout',views.sing_out,name="logout"),
             path('registration',views.registration,name="registration"),
             path('profile',views.profile)]