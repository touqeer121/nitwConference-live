from django.db import models
from django.core.validators import FileExtensionValidator, RegexValidator
from gdstorage.storage import GoogleDriveStorage
gd_storage = GoogleDriveStorage()

class Paper(models.Model) :
	prefix = models.CharField(max_length=20)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	institution = models.CharField(max_length=50)
	email = models.EmailField()
	phone = models.CharField(max_length=10,
							 validators=[RegexValidator(regex=r'[0-9]{10}', message='Invalid Mobile Number')],
							 blank=True)

	paper_title = models.CharField(max_length=300)
	abstract = models.TextField(max_length=500)
	keywords = models.CharField(max_length=500)

	paper_pdf = models.FileField(upload_to='',
								 validators=[FileExtensionValidator(["pdf"])],
								 null=True, blank=True, default=None)

	submission_date = models.DateTimeField()

	def __str__(self):
		return self.paper_title + "(" + str(self.id) + ")"


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