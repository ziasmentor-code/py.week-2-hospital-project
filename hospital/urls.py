from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('departments/', views.department_list, name='department_list'),
    path('department/<int:dept_id>/doctors/', views.department_doctors, name='department_doctors'),

    path('doctors/', views.doctor_list, name='doctor_list'),

    path('bookings/', views.booking_list, name='booking_list'),
    path('bookings/new/', views.booking_create, name='booking_create'),

    path('patients/', views.patient_list, name='patient_list'),
    path('bookings/<int:id>/edit/', views.booking_edit, name='booking_edit'),
path('bookings/<int:id>/delete/', views.booking_delete, name='booking_delete'),

]

