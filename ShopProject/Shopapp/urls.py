from django.urls import path
from . import views

urlpatterns = [
    path('ef/', views.AddEshop.as_view(), name='Eshop_url'),
    path('el/', views.EshopView.as_view(), name='showEshop_url'),
    path('el/<int:page>/', views.EshopView.as_view(), name='showEshop_url'),
    path('ul/<int:pk>/', views.UpdateEshop.as_view(), name='update_url'),
    path('dl/<int:pk>/', views.DeleteEshop.as_view(), name='delete_url'),

    path('hv/', views.Home_View, name='home_url'),
]