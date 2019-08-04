from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path('settings/', views.account_settings, name="account_settings"), #landing page account
    path('login/', views.login_view, name="login"), #login form
    path('signup/', views.signup_view, name="signup"), #signup form
    path('logout/', views.logout_view, name="logout"), #logout
    path('mypage/', views.mypage_view, name="mypage"), #mypage,

]