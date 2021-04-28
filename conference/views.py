import datetime
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import os
import json
import requests

def test_upload(request):
	headers = {
		"Authorization": "Bearer ya29.a0AfH6SMDE18bB4m_ios9jiTJCqZEale8QNeA-JdxL82cQwdxKaLbqS-8YxudmBOLYThO4Z-KWXfgmJK8kKw2GPfU2SI0bwCNTfKXYjmc-5-whSOGGkSMtnmCoJGl99edouMOIN3VidXaxJCzR24Cm3Lxl4NWQ"}
	para = {
		"name": "from_live",
	}
	files = {
		'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
		'file': open("./cat.jpg", "rb")
	}
	r = requests.post(
		"https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
		headers=headers,
		files=files
	)
	print(r.text)

	print("HEY  ",os.getcwd())
	return render(request, 'home.html')



def index(request):
    return render(request, 'home.html')

def about_conference(request):
	return render(request, 'about_conference.html')

def who_should_join(request):
	return render(request, 'who_should_join.html')

def committee(request):
	return render(request, 'committee.html')

def deadlines(request):
	return render(request, 'deadlines.html')

def brochure(request):
	return render(request, 'brochure.html')

def keynote_speakers(request):
	return render(request, 'speakers.html')

def registration(request):
	return render(request, 'register.html')

def early_bird(request):
	return render(request, 'early-bird.html')

def non_early(request):
	return render(request, 'non-early.html')

def call_for_papers(request):
	if(request.method=="POST"):
		ppr = Paper.objects.create(paper_title=request.POST['paper_title'], submission_date=datetime.datetime.now())
		ppr.prefix = request.POST['prefix']
		ppr.first_name = request.POST['fname']
		ppr.last_name = request.POST['lname']
		ppr.institution = request.POST['institution']
		ppr.country = request.POST['country']
		ppr.email = request.POST['email']
		ppr.phone = request.POST['phone']
		ppr.paper_pdf = request.POST['paper_title']
		ppr.abstract = request.POST['abstract']
		ppr.keywords = request.POST['keywords']
		ppr.save()
		messages.success(request, "You've successfully submitted the paper.")
		return redirect('/call_for_papers')
	print("GET method")
	# messages.success(request, "TESTING")
	return render(request, 'online_submission.html')

def abstract_submission(request):
	return render(request, 'abstract_format.html')

def publication_opportunities(request):
	return render(request, 'publication_opportunities.html')

def evaluation_process(request):
	return render(request, 'evaluation_process.html')

def contact_us(request):
	if request.method == 'POST':
		print('Contact us message recieved.')
		newMessage = ContactUsMessage()
		newMessage.sender_name = request.POST['fullName']
		newMessage.email = request.POST['email']
		# newMessage.phone = request.POST['phone']
		newMessage.subject = request.POST['subject']
		newMessage.message = request.POST['message']
		# superuser = CustomUser.objects.filter(is_superuser=True).first()
		# superuser.notifications = superuser.notifications + 1
		# superuser.noti_messages = superuser.noti_messages + '<li> New message has arrived in inbox </li>'
		# superuser.save()
		newMessage.save()
		messages.add_message(request, messages.INFO, 'Your Message has been sent. We will email you back soon.')
		return redirect('/contact_us')
	# print('Contact us message ERROR.')
	return render(request, 'contact_us.html')
