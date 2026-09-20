from django.urls import path
from .import views 
from .views import admin_dashboard
app_name='home'
urlpatterns = [
      #path('home/', views.home, name='home'),
      path('',views.homepage,name='home_page'),
      path('dashboard/', views.dashboard, name='dashboard'),
      path('profile/', views.profile_create, name='profile'),
      path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),
]