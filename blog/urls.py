from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:category_slug>', views.home, name='post_by_category'),
    path('<slug:category_slug>/<slug:post_slug>', views.article_detail, name='post_detail'),

    path('login/', views.loginPage, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutUser, name='logout'),

    path('about/', views.about, name='about'),
]