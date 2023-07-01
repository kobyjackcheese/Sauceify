from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('sauces/', views.SauceList.as_view(), name="sauce_list"),
    path('sauces/new/', views.SauceCreate.as_view(), name="sauce_create"),
    path('sauces/<int:pk>/', views.SauceDetail.as_view(), name="sauce_detail"),
    path('sauces/<int:pk>/update',views.SauceUpdate.as_view(), name="sauce_update"),
    path('sauces/<int:pk>/delete',views.SauceDelete.as_view(), name="sauce_delete"),
]