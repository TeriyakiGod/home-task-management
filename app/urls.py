from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_view, name='list'),
    path('rodzic/', views.list_rodzic_view, name='list_rodzic'),
    path('create/', views.create_duty, name='create'),
    path('change_status/<int:duty_id>/', views.change_status, name='change_status'),
    path('edit_or_delete_duty/<int:duty_id>/', views.edit_or_delete_duty, name='edit_or_delete'),
    path('assign_person_to_duty/<int:duty_id>/', views.assign_person_to_duty, name='assign_person'),
]