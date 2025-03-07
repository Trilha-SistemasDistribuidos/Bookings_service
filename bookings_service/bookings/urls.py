from django.urls import path
from . import views

urlpatterns = [
    path('bookings/', views.BookingCreateListView.as_view(), name='booking-create-list'),
    path('bookings/<int:pk>/', views.BookingRetrieveUpdateDestroyView.as_view(), name='booking-detail-view')
]