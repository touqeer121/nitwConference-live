from django.db import models
from django.core.validators import FileExtensionValidator, RegexValidator
from gdstorage.storage import GoogleDriveStorage
gd_storage = GoogleDriveStorage()

class Abstract(models.Model) :
	abs_id = models.CharField(max_length=20, primary_key=True)
	track = models.CharField(max_length=500)
	prefix = models.CharField(max_length=20)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	institution = models.CharField(max_length=50)
	email = models.EmailField()
	phone = models.CharField(max_length=10,
							 validators=[RegexValidator(regex=r'[0-9]{10}', message='Invalid Mobile Number')],
							 blank=True)

	paper_title = models.CharField(max_length=400)

	abstract_pdf = models.FileField(upload_to='maps',
								validators=[FileExtensionValidator(["pdf", "doc", "docx"])], storage=gd_storage)


	submission_date = models.DateTimeField()

	def __str__(self):
		return self.paper_title + "(" + str(self.abs_id) + ")"



class File(models.Model):
	id = models.AutoField(primary_key=True)
	map_name = models.CharField(max_length=200)
	map_data = models.FileField(upload_to='maps', storage=gd_storage)


class ContactUsMessage(models.Model) :
	sender_name = models.CharField(max_length=50)
	email = models.EmailField()
	phone = models.CharField(max_length=10,
                              validators=[RegexValidator(regex=r'[0-9]{10}', message='Invalid Mobile Number')],
                              blank=True)
	subject = models.CharField(max_length=100)
	message = models.CharField(max_length=1000)
	has_been_read = models.BooleanField(default=False)

	def __str__(self):
		return str(self.id)

class Paper_Count(models.Model):
	paper_count = models.IntegerField(default=0)

	def __unicode__(self):
		return str(self.paper_count)