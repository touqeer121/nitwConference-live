from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
 	path('speakers/', views.speakers, name='speakers'),
    path('registration/', views.registration, name='registration'), 
    path('call_for_papers/', views.call_for_papers, name='call_for_papers'), 
]
