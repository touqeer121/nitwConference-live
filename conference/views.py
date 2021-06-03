import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
import os
import json
import requests
from gdstorage.storage import GoogleDriveStorage, GoogleDrivePermissionType, GoogleDrivePermissionRole, \
	GoogleDriveFilePermission
from django.core.mail import send_mail
from django.conf import settings
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import xlrd
import xlwt
from xlutils.copy import copy
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.staticfiles.storage import staticfiles_storage
from nitwConference.settings import STATIC_URL
import stripe
from django.views.decorators.csrf import csrf_exempt

permission = GoogleDriveFilePermission(
	GoogleDrivePermissionRole.READER,
	GoogleDrivePermissionType.USER,
	'touqeer.pathan289@gmail.com'
)

def registration_payment(request):
	return render(request, 'registration_payment.html')

@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLIC_KEY}
        return JsonResponse(stripe_config, safe=False)

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            print('TRY START')
            # Create new Checkout Session for the order
            # Other optional params include:
            # [billing_address_collection] - to display billing address details on the page
            # [customer] - if you have an existing Stripe Customer ID
            # [payment_intent_data] - capture the payment later
            # [customer_email] - prefill the email input in the form
            # For full details see https://stripe.com/docs/api/checkout/sessions/create

            # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['alipay'],
                mode='payment',
                line_items=[
                    {
                        'name': 'GCIMB Conference Regular Registration',
                        'quantity': 1,
                        'currency': 'inr',
                        'amount': '55',
                    }
                ]
            )
            print('TRY END')
            return JsonResponse({'sessionId': checkout_session.id})
        except Exception as e:
            print('ECXPETION')
            return JsonResponse({'error': str(e)})

			
def success(request):
	return render(request, 'registration_success.html')

def cancelled(request):
	return render(request, 'registration_cancelled.html')

def index(request):
	return render(request, 'home.html')

def about_conference(request):
	return render(request, 'about_conference.html')

def organizing_team(request):
	return render(request, 'organizing_team.html')

def who_should_join(request):
	return render(request, 'who_should_join.html')


def committee(request):
	return render(request, 'committee.html')


def track_chairs(request):
	return render(request, 'track_chairs.html')

def preconference_workshop(request):
	return render(request, 'preconference_workshop.html')


def important_dates(request):
	return render(request, 'deadlines.html')


def brochure(request):
	return render(request, 'brochure.html')


def keynote_speakers(request):
	return render(request, 'speakers.html')


def registration(request):
	return render(request, 'register.html')

def update_sheet(absID):
	# response = HttpResponse(content_type='application/ms-excel')
	# response['Content-Disposition'] = 'attachment; filename="Abstracts.xls"'
	rb = xlrd.open_workbook(settings.PROJECT_PATH+'Abstracts.xls',formatting_info=True)
	r_sheet = rb.sheet_by_index(0) 
	r = r_sheet.nrows
	wb = copy(rb) 
	sheet = wb.get_sheet(0) 

	# file = File.objects.all()
	# if file is None:
	# 	file = File.objects.create()
	# else
	# 	file = file[0]
	ppr = get_object_or_404(Abstract, abs_id=absID)
	sheet.write(r,0,absID)
	sheet.write(r,1,ppr.paper_title)
	sheet.write(r,2,ppr.track)
	sheet.write(r,3,ppr.prefix)
	sheet.write(r,4,ppr.first_name)
	sheet.write(r,5,ppr.last_name)
	sheet.write(r,6,ppr.country)
	sheet.write(r,7,ppr.state)
	sheet.write(r,8,ppr.institution)
	sheet.write(r,9,ppr.email)
	sheet.write(r,10,ppr.phone)
	sheet.write(r,11,str(ppr.abstract_pdf.url)[:-16])
	sheet.write(r,12,str(ppr.submission_date).split()[0])
	wb.save('Abstracts.xls')
	print("SHEET UPDATED\n")

def forward_submission_info(absID):
	ppr = get_object_or_404(Abstract, abs_id=absID)
	msg = MIMEMultipart()
	msg.set_unixfrom('author')
	msg['From'] = settings.EMAIL_HOST_USER
	recipients = ['submissions@gcimb.org', 'rama@gcimb.org', 'ravi@gcimb.org', 'nrustagi@gcimb.org']
	# recipients = ['touqeer.pathan289@gmail.com']
	msg['To'] = ", ".join(recipients)
	msg['Subject'] = 'New Abstract Submitted | Abstract ID : '+absID

	# 'Track : '+ ppr.track + '\n' +\
	message = 'A new abtract has been submitted \n\n' + 'Abstract Details : \n' + \
			'Abstract ID : '+ str(absID) + '\n' + \
			'Author : '+ str(ppr.prefix) + ' ' + str(ppr.first_name) + ' ' + str(ppr.last_name) + '\n' + \
			'Title : '+ str(ppr.paper_title) + '\n' + \
			'Abstract Link : '+ str(ppr.abstract_pdf.url)[:-16] + '\n' + \
			'Address : '+ str(ppr.state) +', '+str(ppr.country) + '\n' + \
			'Institute : '+ str(ppr.institution) + '\n' + \
			'Email : '+ str(ppr.email) + '\n' + \
			'Phone : '+ str(ppr.phone) + '\n' + \
			'Submission Date : '+ str(ppr.submission_date.date()) + '\n' 

	msg.attach(MIMEText(message))
	mailserver = smtplib.SMTP_SSL('smtpout.secureserver.net', 465)
	# mailserver.starttls()
	mailserver.ehlo()
	mailserver.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
	mailserver.sendmail(msg['From'], msg['To'], msg.as_string())
	print("INFO MAIL SENT\n")

def is_duplicate_entry(request):
	oldEntry = Abstract.objects.filter(paper_title=request.POST['title'], first_name=request.POST['fname'], last_name=\
	request.POST['lname'], institution= request.POST['institution'])
	return (len(oldEntry)> 0)

def abstract_submission(request):
	if (request.method == "POST"):
		duplicate = is_duplicate_entry(request)
		if not duplicate:
			doc=request.FILES
			file_pdf = doc['pdf']
			cnt = Paper_Count.objects.get()
			year = datetime.datetime.now().year
			yy = str(year)
			p1 = yy[2:]
			p2 = str(cnt.paper_count).zfill(4)
			cnt.paper_count = cnt.paper_count + 1
			cnt.save()
			absID = "GCIMB" + p1 + p2
			ppr = Abstract.objects.create(abs_id=absID, submission_date=datetime.datetime.now(), abstract_pdf=file_pdf)
			ppr.track = request.POST['track']
			ppr.prefix = request.POST['prefix']
			ppr.first_name = request.POST['fname']
			ppr.last_name = request.POST['lname']
			ppr.institution = request.POST['institution']
			ppr.country = request.POST['country']
			ppr.state = request.POST['state']
			ppr.email = request.POST['email']
			ppr.phone = request.POST['phone']
			ppr.paper_title = request.POST['title']
			# print("TITLE iS: ", request.POST['title'])
			ppr.save()
	
		msg = MIMEMultipart()
		msg.set_unixfrom('author')
		msg['From'] = settings.EMAIL_HOST_USER
		msg['To'] = request.POST['email']

		if not duplicate:
			msg['Subject'] = 'Abstract submission acknowledgement'
			message = 'Hello ' + ppr.prefix + ' ' + ppr.first_name + ' ' + ppr.last_name + ',\n\n' + \
					'Hope you are safe and doing well. This is to acknowledge that we have received your abstract.' + \
					'Your abstract ID will be ' + absID +'. Please make a note of it and quote the same in future communications.\n\n' + \
					'Your abstract will be sent for review and you should be hearing from us very soon on the next steps.\n\n' + \
					'Many thanks for considering to submit your work to GCIMB.\n\n'+\
					'Best Regards,\n' + \
					'Organizing Team,\n' + \
					'Global Conference on Innovations in Management and Business'
		else:
			msg['Subject'] = 'Abstract already submitted'
			abs_id = get_object_or_404(Abstract, paper_title=request.POST['title']).abs_id
			if abs_id is None:
				message = 'Looks like your abstract with the title \"'+str(request.POST['title'])+'\" is already ' + \
				'submitted and you should receive an an email. \nIn case you didn’t, please write to submissions@gcimb.org quoting your details.'	
			else:	
				message = 'Looks like your abstract with the title \"'+str(request.POST['title'])+'\" (Abstract ID : ' + str(abs_id) + ') is already ' + \
				'submitted and you should receive an an email. \nIn case you didn’t, please write to submissions@gcimb.org quoting your details.'	
		
		msg.attach(MIMEText(message))

		mailserver = smtplib.SMTP_SSL('smtpout.secureserver.net', 465)
		# mailserver.starttls()
		mailserver.ehlo()
		mailserver.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
		mailserver.sendmail(msg['From'], msg['To'], msg.as_string())

		if not duplicate:
			update_sheet(absID)
			forward_submission_info(absID)
			messages.success(request, "You've successfully submitted the abstract.")
		else:
			messages.success(request, "You've already submitted an abstract with this title.")
		print("EVRYTHING DONE\n")
		return redirect('/abstract-submission')
	return render(request, 'abstract_submission.html')

def early_bird(request):
	return render(request, 'early-bird.html')


def non_early(request):
	return render(request, 'non-early.html')


def call_for_papers(request):
	return render(request, 'call_for_papers.html')


def abstract_submission_guidelines(request):
	return render(request, 'abstract_submission_guidelines.html')


def publication_opportunities(request):
	return render(request, 'publication_opportunities.html')


def evaluation_process(request):
	return render(request, 'evaluation_process.html')


def contact_us(request):
	if request.method == 'POST':
		msg = MIMEMultipart()
		msg.set_unixfrom('author')
		msg['From'] = 'info@gcimb.org'
		msg['To'] = request.POST['email']
		msg['Subject'] = request.POST['subject']
		message = request.POST['message']
		msg.attach(MIMEText(message))

		mailserver = smtplib.SMTP_SSL('smtpout.secureserver.net', 465)
		# mailserver.starttls()
		mailserver.ehlo()
		mailserver.login('info@gcimb.org', 'info123@gcimb')

		mailserver.sendmail(msg['From'], msg['To'], msg.as_string())

		mailserver.quit()
		messages.success(request, "Message Sent successfully. We'll get back to you soon.")
		return redirect('/contact_us')
	# messages.success(request, "testing bro")
	return render(request, 'contact_us.html')


def export_abstracts_sheet(request):
	response = HttpResponse(content_type='application/ms-excel')
	response['Content-Disposition'] = 'attachment; filename="Abstracts.xls"'
	wb = xlwt.Workbook(encoding='utf-8')
	ws = wb.add_sheet('Abstracts')
	
	# Sheet header, first row
	row_num = 0
	
	font_style = xlwt.XFStyle()
	font_style.font.bold = True
	columns = ['Abstract ID', 'Title', 'Track', 'Prefix', 'First Name', 'Last Name', 'Country', 'State', \
			'Institute', 'Email', 'Phone', 'File Name', 'File Link', 'Submission Date']		
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)
	
	# Sheet body, remaining rows
	font_style = xlwt.XFStyle()
	
	rows = Abstract.objects.all().values_list('abs_id', 'paper_title', 'track', 'prefix', 'first_name', 'last_name', 'country', 'state',\
			 'institution', 'email', 'phone', 'abstract_pdf', 'submission_date' )

	counter = 0
	for row in rows:
		row_num += 1
		for col_num in range(len(row)):
			if col_num==13:
				dt = str(row[col_num]).split()[0]
				ws.write(row_num, col_num, dt, font_style)
			elif col_num==11:
				ppr = get_object_or_404(Abstract, abs_id=row[0])
				if ppr:
					ws.write(row_num, col_num, str(ppr.abstract_pdf), font_style)
			elif col_num==12:
				ppr = get_object_or_404(Abstract, abs_id=row[0])
				if ppr:
					ws.write(row_num, col_num, str(ppr.abstract_pdf.url)[:-16], font_style)
			else:
				ws.write(row_num, col_num, row[col_num], font_style)
		counter += 1
	wb.save(response)
	return response