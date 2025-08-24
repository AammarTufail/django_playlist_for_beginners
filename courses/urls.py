from django.urls import path
from . import views

urlpatterns = [
        path('<int:pk>/', views.course_detail, name='course_detail'),
]