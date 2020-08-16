from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:name>', views.sub, name='subject'),
    path('/<str:n>', views.topic, name='topic'),
]