from django.urls import path

from . import views

app_name = "account"

urlpatterns = [
    path('settings/', views.settings_view, name="settings"), #landing page account
    path('password/', views.change_password, name="change_password"), #landing page account
    path('login/', views.login_view, name="login"), #login form
    path('signup/', views.signup_view, name="signup"), #signup form
    path('logout/', views.logout_view, name="logout"), #logout
    path('mypage/', views.mypage_view, name="mypage"), #mypage,
    path('resetpass/<str:uidb64>/<str:token>', views.resetpass_view, name = "resetpass"),
    path('forgotpass/', views.forgotpass_view, name = "forgotpass"),
    path('activate/<str:uidb64>/<str:token>', views.activate, name="activate"),

]