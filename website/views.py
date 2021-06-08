from django.shortcuts import render
from django.core.mail import send_mail



def home(request):
	return render(request, "home.html", {})


def contact(request):
	if request.method == "POST":
		name = request.POST.get('name', False)
		email  = request.POST.get('email', False)
		subject = request.POST.get('subject', False)
		message = request.POST.get('message', False)


		return render(request, 'contact.html', {'name': name})

		send_mail(
			subject,
			message,
			name,
			email,
			['zurabsx@gmail.com'],
		)

	else:
		return render(request, "contact.html", {})


def about(request):
	return render(request, "about.html", {})



def service(request):
	return render(request, "service.html", {})



def team(request):
	return render(request, "team.html", {})


def portfolio(request):
	return render(request, "portfolio.html", {})




	