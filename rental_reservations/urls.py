from django.urls import path
from django.urls import include
#now import the views.py file into this code
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('reservations/', views.ReservationListView.as_view(), name='reservations'),
    path('reservation/<uuid:pk>/', views.reservation_detail, name='reservation_detail'),
    path('rentals/', views.RentalListView.as_view(), name='rentals'),
    path('rental/<uuid:pk>/', views.rental_detail, name='rental_detail'),
    
]