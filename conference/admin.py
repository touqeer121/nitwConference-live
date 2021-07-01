from django.contrib import admin
from .models import *


admin.site.register(Abstract)
admin.site.register(Paper)
admin.site.register(Ppt)
admin.site.register(Registration_Type)
admin.site.register(Author_Type)
admin.site.register(Registration)
admin.site.register(ContactUsMessage)
admin.site.register(File)
admin.site.register(Paper_Count)
admin.site.register(Ppt_Count)
admin.site.register(Registration_Count)
admin.site.register(Full_Paper_Count)
admin.site.register(ReceivedException)
admin.site.register(EmailQueue)
admin.site.register(EmailInfo)
admin.site.register(Receipt)
# admin.site.register(Query)