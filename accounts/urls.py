from django.urls import path, include
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	# url(r'^register/(?P<alias>[A-Za-z0-9.-]+)/$',views.register,name='register'),
	url(r'^sign-in/$',views.signin,name='signin'),
    url(r'^sign-out/$',views.signout,name='signout'),
	# url(r'^signout/(?P<alias>[A-Za-z0-9.-]+)/$',views.signout,name='signout'),   
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
