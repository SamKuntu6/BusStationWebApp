from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name="home"),
    path('index/', views.manager_homepage, name="index"),
    path('busstanddata/', views.stand_data, name="stand_data"),
    path('revenue/', views.revenue_page, name="revenue"),
    path('login/', views.login_page, name="login_page"),
    path('logout/', views.logout_user, name="logout")
]

# placed in the future in case doesnt work

# path('register/', views.register_page, name="register_page"),