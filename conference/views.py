import datetime
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def index(request):
    return render(request, 'home.html')

def speakers(request):
	return render(request, 'speakers.html')

def registration(request):
	return render(request, 'register.html')

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
