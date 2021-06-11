from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

def signin(request):
    response = {}
    if request.user.is_authenticated:
	    return redirect('/')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if username is not 'gcimb':
                messages.success(request, "Welcome on board! Please switch to 'Review Abstracts' tab to review the abtracts submitted under your corresponding track.")
                request.session['count'] = 0
            else:
                messages.success(request, "You've successfully signed in.")
                request.session['count'] = 1
            return redirect('/')
        else:
            if 'count' in request.session:
              del request.session['count']
            messages.success(request, "Invalid Credentials.")
    return render(request,'sign_in.html',response)

def signout(request):
    logout(request)
    if 'count' in request.session:
        del request.session['count']
    messages.success(request, "You've successfully signed out.")
    return redirect('/')

    
