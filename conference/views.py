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

permission = GoogleDriveFilePermission(
	GoogleDrivePermissionRole.READER,
	GoogleDrivePermissionType.USER,
	'touqeer.pathan289@gmail.com'
)
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

def forward_submission_info(absID):
	ppr = get_object_or_404(Abstract, abs_id=absID)
	msg = MIMEMultipart()
	msg.set_unixfrom('author')
	msg['From'] = settings.EMAIL_HOST_USER
	recipients = ['info@gcimb.org', 'rama@gcimb.org', 'ravi@gcimb.org', 'nrustagi@gcimb.org']
	msg['To'] = ", ".join(recipients)
	msg['Subject'] = 'New Abstract Submitted | Abstract ID : '+absID

	# 'Track : '+ ppr.track + '\n' +\
	message = 'A new abtract has been submitted \n\n' + 'Abstarct Details : \n' + \
			'Abstract ID : '+ str(absID) + '\n' + \
			'Author : '+ str(ppr.prefix) + ' ' + str(ppr.first_name) + ' ' + str(ppr.last_name) + '\n' + \
			'Title : '+ str(ppr.paper_title) + '\n' + \
			'Abstract Link : '+ str(ppr.abstract_pdf.url) + '\n' + \
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
	mailserver.sendmail(msg['From'], recipients, msg.as_string())

def abstract_submission(request):
	if (request.method == "POST"):
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
		msg['Subject'] = 'Abstract submission acknowledgement'

		message = 'Hello ' + ppr.prefix + ' ' + ppr.first_name + ' ' + ppr.last_name + ',\n\n' + \
				  'Hope you are safe and doing well. This is to acknowledge that we have received your abstract.' + \
				  'Your abstract ID will be ' + absID +'. Please make a note of it and quote the same in future communications.\n\n' + \
				  'Your abstract will be sent for review and you should be hearing from us very soon on the next steps.\n\n' + \
				  'Many thanks for considering to submit your work to GCIMB.\n\n'+\
				  'Best Regards,\n' + \
				  'Organizing Team,\n' + \
				  'Global Conference on Innovations in Management and Business'
		msg.attach(MIMEText(message))

		mailserver = smtplib.SMTP_SSL('smtpout.secureserver.net', 465)
		# mailserver.starttls()
		mailserver.ehlo()
		mailserver.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
		mailserver.sendmail(msg['From'], msg['To'], msg.as_string())

		messages.success(request, "You've successfully submitted the abstract.")
		forward_submission_info(absID)

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