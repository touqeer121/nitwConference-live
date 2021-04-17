from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about_conference/', views.about_conference, name='about_conference'),
    path('committee/', views.committee, name='committee'),
    path('deadlines/', views.deadlines, name='deadlines'),
    path('brochure/', views.brochure, name='brochure'),
 	path('keynote_speakers/', views.keynote_speakers, name='keynote_speakers'),
    path('registration/', views.registration, name='registration'), 
    path('call_for_papers/', views.call_for_papers, name='call_for_papers'),
    path('abstract_format/', views.abstract_format, name='abstract_format'),
    path('full_paper_format/', views.full_paper_format, name='full_paper_format'),
    path('review_process/', views.review_process, name='review_process'),
]
