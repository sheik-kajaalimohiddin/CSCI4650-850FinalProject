from django.contrib.auth import admin
from django.urls import path, include

from CSCI4650850FinalProjectapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('upload/', views.upload_image, name='upload_image'),
    path('search/', views.search_image, name='search_image'),
    path('delete_image/<str:pk>', views.delete_image, name='delete_image'),
    path('about/', views.about, name='about'),
    path('local_search/', views.local_search, name='local_search'),
    path('detailed_view/<str:pk>/', views.detailedView, name='image-detailed-view'),
    path('search_type_listings/', views.ImageTypeSearchView.as_view(), name='image-type'),
]
