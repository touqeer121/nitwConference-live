from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('callback/', views.callback, name='callback'),
    path('', views.index, name='index'),
    path('abstract-submission/', views.abstract_submission, name='abstract_submission'),
    path('about-conference/', views.about_conference, name='about_conference'),
    path('who-can-join/', views.who_should_join, name='who_should_join'),
    path('committee/', views.committee, name='committee'),
    path('track-chairs/', views.track_chairs, name='track_chairs'),
    path('preconference-workshop/', views.preconference_workshop, name='preconference_workshop'),
    path('important-dates/', views.important_dates, name='important_dates'),
    path('brochure/', views.brochure, name='brochure'),
 	path('keynote-speakers/', views.keynote_speakers, name='keynote_speakers'),
    path('registration/', views.registration, name='registration'),
    path('registration/early-bird', views.early_bird, name='early_bird'),
    path('registration/non-early', views.non_early, name='non_early'),
    path('call-for-papers/', views.call_for_papers, name='call_for_papers'),
    path('abstract-submission-guidelines/', views.abstract_submission_guidelines, name='abstract_submission_guidelines'),
    path('publication-opportunities/', views.publication_opportunities, name='publication_opportunities'),
    path('evaluation-process/', views.evaluation_process, name='evaluation_process'),
    path('contact-us/', views.contact_us, name='contact_us'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
