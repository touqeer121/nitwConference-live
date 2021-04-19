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
    path('registration/early-bird', views.early_bird, name='early_bird'),
    path('registration/non-early', views.non_early, name='non_early'),
    path('call_for_papers/', views.call_for_papers, name='call_for_papers'),
    path('abstract_format/', views.abstract_format, name='abstract_format'),
    path('full_paper_format/', views.full_paper_format, name='full_paper_format'),
    path('review_process/', views.review_process, name='review_process'),
    path('contact_us/', views.contact_us, name='contact_us'),
]
