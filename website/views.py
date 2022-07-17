from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.


def home(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		Phone = request.POST['Phone']
		Email = request.POST['Email']
		Message = request.POST['Message']
		# send an email
		send_mail(
			message_name, #subject
			Message, #message
			Email, # fromm email
			["ard.international.corp@gmail.com"], # to email
			)
		return render(request, 'home.html', {"message_name": message_name})

	else:

		return render(request, 'home.html', {})
