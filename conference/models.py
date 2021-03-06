from django.db import models
from django.core.validators import FileExtensionValidator, RegexValidator
from gdstorage.storage import GoogleDriveStorage
from django.utils import timezone
gd_storage = GoogleDriveStorage()

class Abstract(models.Model) :
	abs_id = models.CharField(max_length=100, primary_key=True)
	track = models.CharField(max_length=500)
	prefix = models.CharField(max_length=100)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	is_finally_approved = models.BooleanField(blank=True, default=False)
	is_finally_rejected = models.BooleanField(blank=True, default=False)
	remark = models.CharField(max_length=5000, blank=True, default='')
	is_approved_by_A = models.BooleanField(blank=True, default=False)
	is_rejected_by_A = models.BooleanField(blank=True, default=False)
	is_approved_by_B = models.BooleanField(blank=True, default=False)
	is_rejected_by_B = models.BooleanField(blank=True, default=False)
	status_C = models.CharField(max_length=1, blank=True, default='2')
	remark_A = models.CharField(max_length=5000, blank=True, default='')
	remark_B = models.CharField(max_length=5000, blank=True, default='')
	remark_C = models.CharField(max_length=5000, blank=True, default='')
	track_A = models.CharField(max_length=5000, blank=True, null=True, default='A')
	track_B = models.CharField(max_length=5000, blank=True, null=True, default='admin')
	country = models.CharField(max_length=5000, blank=True, null=True, default='undefined')
	state = models.CharField(max_length=500, blank=True, null=True, default='undefined')
	institution = models.CharField(max_length=1000)
	email = models.EmailField()
	phone = models.CharField(max_length=100,
							 validators=[RegexValidator(regex=r'[0-9]{10}', message='Invalid Mobile Number')],
							 blank=True)

	paper_title = models.CharField(max_length=500)

	abstract_affiliation_pdf = models.FileField(upload_to='maps',
								validators=[FileExtensionValidator(["pdf"])], storage=gd_storage, null=True)

	abstract_pdf = models.FileField(upload_to='maps',
								validators=[FileExtensionValidator(["pdf"])], storage=gd_storage, null=True)

	# abstract_url = models.CharField(max_length=5000, blank=True, default='unknown')

	submission_date = models.DateTimeField()

	def __str__(self):
		return self.paper_title + "(" + str(self.abs_id) + ")"

#pass key
class Paper(models.Model) :
	paper_id = models.CharField(max_length=100, primary_key=True)
	abstract = models.ForeignKey(Abstract, verbose_name="Abstract", on_delete=models.CASCADE, blank=True, null=True)
	track = models.CharField(max_length=500)
	prefix = models.CharField(max_length=100)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	status = models.CharField(max_length=1, blank=True, default='2')
	status_A = models.CharField(max_length=1, blank=True, default='2')
	status_B = models.CharField(max_length=1, blank=True, default='2')
	remark = models.CharField(max_length=5000, blank=True, default='')
	remark_A = models.CharField(max_length=5000, blank=True, default='')
	remark_B = models.CharField(max_length=5000, blank=True, default='')
	track_A = models.CharField(max_length=5000, blank=True, null=True, default='A')
	track_B = models.CharField(max_length=5000, blank=True, null=True, default='admin')
	country = models.CharField(max_length=5000, blank=True, null=True, default='undefined')
	state = models.CharField(max_length=500, blank=True, null=True, default='undefined')
	institution = models.CharField(max_length=1000)
	email = models.EmailField()
	phone = models.CharField(max_length=100,
							 validators=[RegexValidator(regex=r'[0-9]{10}', message='Invalid Mobile Number')],
							 blank=True)

	paper_title = models.CharField(max_length=500)

	paper_affiliation_pdf = models.FileField(upload_to='maps',
								validators=[FileExtensionValidator(["pdf"])], storage=gd_storage, null=True)
	paper_manuscript_pdf = models.FileField(upload_to='maps',
								validators=[FileExtensionValidator(["pdf"])], storage=gd_storage, null=True)
	submission_date = models.DateTimeField()

	def __str__(self):
		return self.paper_title + "(" + str(self.paper_id) + ")"


class Ppt(models.Model) :
	ppt_id = models.CharField(max_length=100, primary_key=True)
	abstract = models.ForeignKey(Abstract, verbose_name="Abstract", on_delete=models.CASCADE, blank=True, null=True)
	track = models.CharField(max_length=500)
	prefix = models.CharField(max_length=100)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	status = models.CharField(max_length=1, blank=True, default='2')
	status_A = models.CharField(max_length=1, blank=True, default='2')
	status_B = models.CharField(max_length=1, blank=True, default='2')
	remark = models.CharField(max_length=5000, blank=True, default='')
	remark_A = models.CharField(max_length=5000, blank=True, default='')
	remark_B = models.CharField(max_length=5000, blank=True, default='')
	track_A = models.CharField(max_length=5000, blank=True, null=True, default='A')
	track_B = models.CharField(max_length=5000, blank=True, null=True, default='admin')
	country = models.CharField(max_length=5000, blank=True, null=True, default='undefined')
	state = models.CharField(max_length=500, blank=True, null=True, default='undefined')
	institution = models.CharField(max_length=1000)
	email = models.EmailField()
	phone = models.CharField(max_length=100,
							 validators=[RegexValidator(regex=r'[0-9]{10}', message='Invalid Mobile Number')],
							 blank=True)

	ppt_title = models.CharField(max_length=500)

	ppt_pdf = models.FileField(upload_to='maps',
								validators=[FileExtensionValidator(["ppt", "pptx"])], storage=gd_storage)
	submission_date = models.DateTimeField()

	def __str__(self):
		return self.ppt_title + "(" + str(self.ppt_id) + ")"


class Registration_Type(models.Model) :
	id = models.AutoField(primary_key=True)
	registration_type = models.CharField(max_length=100)
	def __str__(self):
		return self.registration_type +" (" + str(self.id) + ")"


class Author_Type(models.Model) :	
	id = models.AutoField(primary_key=True)
	author_type = models.CharField(max_length=100)
	def __str__(self):
		return self.author_type +" (" + str(self.id) + ")"


class Registration(models.Model) :
	registration_id = models.CharField(max_length=100, primary_key=True)
	registration_type = models.ForeignKey(Registration_Type, verbose_name="Registration_Type", on_delete=models.CASCADE, blank=True, null=True)
	author_type = models.ForeignKey(Author_Type, verbose_name="Author_Type", on_delete=models.CASCADE, blank=True, null=True)
	payment_method = models.CharField(max_length=200, blank=True, default='unknown')
	transaction_id = models.CharField(max_length=100, blank=True, default='unknown')
	abstract = models.ForeignKey(Abstract, verbose_name="Abstract", on_delete=models.CASCADE, blank=True, null=True)
	prefix = models.CharField(max_length=100, blank=True, null=True)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100, blank=True, null=True)
	id_status = models.CharField(max_length=1, blank=True, default='2')
	payment_status =  models.CharField(max_length=1, blank=True, default='2')
	country = models.CharField(max_length=5000, blank=True, null=True, default='undefined')
	state = models.CharField(max_length=500, blank=True, null=True, default='undefined')
	institution = models.CharField(max_length=1000)
	email = models.EmailField()
	phone = models.CharField(max_length=100,
							 validators=[RegexValidator(regex=r'[0-9]{10}', message='Invalid Mobile Number')],
							 blank=True)

	id_proof = models.FileField(upload_to='maps', validators=[FileExtensionValidator(["png", "pdf", "jpeg", "jpg"])], 
								storage=gd_storage, blank=True, null=True, default='undefined')
	remark = models.CharField(max_length=5000, blank=True, default='')
	registration_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.first_name + ' : (' + str(self.registration_id) + ")"


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

class Ppt_Count(models.Model):
	ppt_count = models.IntegerField(default=0)

	def __unicode__(self):
		return str(self.ppt_count)

class Registration_Count(models.Model):
	registration_count = models.IntegerField(default=0)

	def __unicode__(self):
		return str(self.registration_count)

class Full_Paper_Count(models.Model):
	full_paper_count = models.IntegerField(default=0)

	def __unicode__(self):
		return str(self.full_paper_count)

class ReceivedException(models.Model):
	function_name =  models.CharField(max_length=1000, blank=True, default='unknown')
	corresponding_id =  models.CharField(max_length=1000, blank=True, default='unknown')
	exception_args =  models.CharField(max_length=10000, blank=True, default='unknown')
	exception_message =  models.CharField(max_length=10000, blank=True, default='unknown')
	general_info =  models.CharField(max_length=10000, blank=True, default='unknown')
	current_user_info =  models.CharField(max_length=10000, blank=True, default='unknown')
	exception_date = models.DateTimeField(default=timezone.now)

	def __unicode__(self):
		return str(self.id) + funcName
	
class EmailQueue(models.Model):
	corresponding_id =  models.CharField(max_length=1000, blank=True, default='unknown')
	mail_reason =  models.CharField(max_length=10000, blank=True, default='unknown')
	general_info =  models.CharField(max_length=10000, blank=True, default='unknown')
	pending_date = models.DateTimeField(default=timezone.now)

	def __unicode__(self):
		return str(self.id) + corresponding_id

class EmailInfo(models.Model):
	corresponding_id =  models.CharField(max_length=1000, blank=True, default='unknown')
	mail_reason =  models.CharField(max_length=10000, blank=True, default='unknown')
	general_info =  models.CharField(max_length=10000, blank=True, default='unknown')
	sent_date = models.DateTimeField(default=timezone.now)

	def __unicode__(self):
		return str(self.id) + corresponding_id
	

class Receipt(models.Model) :
	registration = models.OneToOneField(Registration, verbose_name="Registration", primary_key=True, related_name='Receipt', 
								on_delete=models.CASCADE)

	receipt_file = models.FileField(upload_to='receipts', validators=[FileExtensionValidator(["png", "pdf", "jpeg", "jpg"])], 
								storage=gd_storage, blank=True, null=True, default='undefined')

	def __str__(self):
		return str(self.registration.registration_id) + '(Receipt)'


class Query(models.Model):
	asked_to = models.CharField(max_length=500, blank=True, default='unknown')
	name =  models.CharField(max_length=500, blank=True, default='unknown')
	registration_id = models.CharField(max_length=100, blank=True, default='unknown')
	email = models.EmailField()
	query =  models.CharField(max_length=50000, blank=True, default='unknown')
	institution =  models.CharField(max_length=10000, blank=True, default='unknown')
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return str(self.id) + '.' + self.name + ' => ' +  self.asked_to + ' : ' + self.query