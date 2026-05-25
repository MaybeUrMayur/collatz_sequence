from django.urls import path
from . import views

urlpatterns = [
    path('', views.collatz_view, name='collatz'),
    path('collatz/', views.collatz_api, name='collatz_api'),
    path('history/', views.collatz_history, name='collatz_history'),
    path('history/<int:history_id>/', views.collatz_history_detail, name='collatz_history_detail'),
]
