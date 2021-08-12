from django.urls import path, include
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('callback/', views.callback, name='callback'),
    # url(r'login/$', views.user_login, name='login'),    
    path('', views.index, name='index'),
    path('update_sheet/', views.update_sheet, name='update_sheet'),
    path('remark-abstracts/<int:pgNo>', views.remark_abstracts, name='remark_abstracts'),
    path('remark-abstracts/', views.remark_abstracts, name='remark_abstracts'),
    path('registration/', views.registration, name='registration'),
    path('registration-approval/<int:pgNo>', views.registration_approval, name='registration_approval'),
    path('registration-approval/', views.registration_approval, name='registration_approval'),
    path('abstract-submission/', views.abstract_submission, name='abstract_submission'),
    path('paper-submission/', views.paper_submission, name='paper_submission'),
    path('ppt-submission/', views.ppt_submission, name='ppt_submission'),
    path('about-conference/', views.about_conference, name='about_conference'),
    path('organizing-team/', views.organizing_team, name='organizing_team'),
    path('who-can-join/', views.who_should_join, name='who_should_join'),
    path('committee/', views.committee, name='committee'),
    path('track-chairs/', views.track_chairs, name='track_chairs'),
    path('session-chairs/', views.session_chairs, name='session_chairs'),
    path('preconference-workshop/', views.preconference_workshop, name='preconference_workshop'),
    path('important-dates/', views.important_dates, name='important_dates'),
    path('brochure/', views.brochure, name='brochure'),
 	path('keynote-speakers/', views.keynote_speakers, name='keynote_speakers'),
    path('registration-payment/', views.registration_payment, name='registration_payment'),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    path('success', views.success, name='success'),
    path('cancelled', views.cancelled, name='cancelled'),
    path('registration/early-bird', views.early_bird, name='early_bird'),
    path('registration/non-early', views.non_early, name='non_early'),
    path('call-for-papers/', views.call_for_papers, name='call_for_papers'),
    path('digital-transformation-and-information-systems/', views.digital_transformation_and_information_systems),
    path('abstract-submission-guidelines/', views.abstract_submission_guidelines, name='abstract_submission_guidelines'),
    path('publication-opportunities/', views.publication_opportunities, name='publication_opportunities'),
    path('evaluation-process/', views.evaluation_process, name='evaluation_process'),
    path('contact-us/', views.contact_us, name='contact_us'),
    # path('export/xls/', views.export_presentations_sheet, name='export_presentations_sheet'),
    path('export/xls/', views.export_papers_sheet, name='export_papers_sheet'),
    path('exportr/xls/', views.export_registrations_sheet, name='export_registrations_sheet'),

    url('approveabstract/(?P<abstractid>\w+)', views.approve_abstract, name='approve_abstract'),
    url('rejectabstract/(?P<abstractid>\w+)', views.reject_abstract, name='reject_abstract'),
    url('removeremarks/(?P<abstractid>\w+)', views.remove_remark, name='remove_remark'),

    url('approveid/(?P<registrationid>\w+)', views.approve_id, name='approve_id'),
    url('rejectid/(?P<registrationid>\w+)', views.reject_id, name='reject_id'),
    url('resetdecisionforid/(?P<registrationid>\w+)', views.reset_decision_for_id, name='reset_decision_for_id'),

    url('approvepayment/(?P<registrationid>\w+)', views.approve_payment, name='approve_payment'),
    url('rejectpayment/(?P<registrationid>\w+)', views.reject_payment, name='reject_payment'),
    url('resetdecisionforpayment/(?P<registrationid>\w+)', views.reset_decision_for_payment, name='reset_decision_for_payment'),
    
    path('test-doc/', views.test_doc, name='test_doc'),
    url('generate-receipt/(?P<registrationid>\w+)', views.generate_receipt, name='generate_receipt'),
    
    path('test-mail/', views.test_mail, name='test_mail'),
    url('send-approval-mail/(?P<registrationid>\w+)', views.send_approval_mail, name='send_approval_mail'),

    path('biggie-bills/', views.biggie_bills, name='biggie_bills'),

    path('ask-the-editors/', views.ask_the_editors, name='ask_the_editors'),
    path('storeURL/<int:end>', views.storeURL, name='storeURL'),
    
    path('programme-schedule/', views.programme_schedule, name='programme_schedule'),
    path('best-papers/', views.best_papers, name='best_papers'),
    path('feedback-forms/', views.feedback_forms, name='feedback_forms'),
    path('book-of-abstracts/', views.book_of_abstracts, name='book_of_abstracts'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
